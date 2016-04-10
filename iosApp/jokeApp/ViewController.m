//
//  ViewController.m
//  jokeApp
//
//  Created by Patrick Wilson on 4/7/16.
//  Copyright © 2016 Patrick Wilson. All rights reserved.
//

#import "ViewController.h"
#import <MHTextSearch/MHSearchResultItem.h>
#import <MHTextSearch/MHTextSearch.h>
#import <MHTextSearch/MHTextIndex.h>
#import "CHCSVParser.h"
#import "JokeListTableViewController.h"
#import "JokeShowCaseViewController.h"

#import "MyManager.h"
#import <UIKit/UIKit.h>


@interface ViewController ()

@property (nonatomic,strong) MHTextIndex *index;
@property (nonatomic) CGFloat x,y,z;
@property (nonatomic) BOOL xup,yup,zup;
@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    self.index = [[MyManager sharedManager] sharedIndex];
    
    _xup = YES;
    _yup = YES;
    _zup = YES;
    [NSTimer scheduledTimerWithTimeInterval:0.03f target:self selector:@selector(someMethod) userInfo:nil repeats:YES];
    
    
   
    
    [self.navigationController.navigationBar setTitleTextAttributes:
     @{NSForegroundColorAttributeName:[UIColor blackColor],NSFontAttributeName:[UIFont fontWithName:@"AvenirNext-Regular" size:20.0f]}];
    
    
    
        // Do any additional setup after loading the view, typically from a nib.
}
- (void)someMethod
{
    
    self.view.backgroundColor = [UIColor colorWithRed:_x green:_y blue:_z alpha:1.0f];
    
    CGFloat xFloat = [self randomFloatBetween:.001 and:.015];
    CGFloat yFloat = [self randomFloatBetween:.001 and:.015];
    CGFloat zFloat = [self randomFloatBetween:.001 and:.015];
    
    _x += (_xup)? xFloat : -xFloat;
    _y += (_yup)? yFloat : -yFloat;
    _z += (_zup)? zFloat : -zFloat;
    
    if(_x >= 1)
        _xup = NO;
    if(_y >= 1)
        _yup = NO;
    if(_z >= 1)
        _zup = NO;
    
    if(_x <= .0)
        _xup = YES;
    if(_y <= .0)
        _yup = YES;
    if(_z <= .0)
        _zup = YES;
}


- (float)randomFloatBetween:(float)smallNumber and:(float)bigNumber {
    float diff = bigNumber - smallNumber;
    return (((float) (arc4random() % ((unsigned)RAND_MAX + 1)) / RAND_MAX) * diff) + smallNumber;
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (IBAction)pressed:(id)sender {
    
    UIAlertController *alertController = [UIAlertController
                                          alertControllerWithTitle:@"Enter a topic"
                                          message:@"and we will find a joke about it"
                                          preferredStyle:UIAlertControllerStyleAlert];
    
    [alertController addTextFieldWithConfigurationHandler:^(UITextField *textField)
     {
         textField.placeholder = NSLocalizedString(@"Enter topic here", @"Login");
     }];
    
    UIAlertAction *cancelAction = [UIAlertAction
                                   actionWithTitle:NSLocalizedString(@"Cancel", @"Cancel action")
                                   style:UIAlertActionStyleCancel
                                   handler:^(UIAlertAction *action)
                                   {
                                       NSLog(@"Cancel action");
                                   }];
    
    UIAlertAction *okAction = [UIAlertAction
                               actionWithTitle:NSLocalizedString(@"OK", @"OK action")
                               style:UIAlertActionStyleDefault
                               handler:^(UIAlertAction *action)
                               {
                                   UITextField *login = alertController.textFields.firstObject;
                                   NSArray* result = [self.index searchResultForKeyword:login.text options:NSEnumerationConcurrent];
                                   
                                   if ([result count] >0){
                                       NSMutableArray *resultArray = [NSMutableArray new];
                                       for (id item in result){
                                           MHSearchResultItem *result = (MHSearchResultItem*)item;
                                           NSString *jokeString =result.context[@"title"];
                                           NSArray *tempArray = [NSArray arrayWithObjects:jokeString,jokeString,nil];
                                           [resultArray addObject:tempArray];
                                       }
                                       
                                       if ([resultArray count]>20){
                                           resultArray = [[resultArray subarrayWithRange: NSMakeRange( 0, 20 )] mutableCopy];
                                       }
                                       
//                                       NSLog(@"%@",top.context[@"title"]);
                                       
                                       JokeListTableViewController *vc = [self.storyboard instantiateViewControllerWithIdentifier:@"topJokeVC"];
                                       
                                       NSArray *itemsForView = (NSArray*)resultArray;
                                       //    for (id thing in itemsForView){
                                       //        NSArray *tmp = (NSArray*)thing;
                                       //        NSString *jokeString = [tmp objectAtIndex:1];
                                       //        jokeString = [jokeString stringByReplacingOccurrencesOfString:@" |||" withString:@"."];
                                       //    }
                                       UIBarButtonItem *newBackButton =
                                       [[UIBarButtonItem alloc] initWithTitle:@""
                                                                        style:UIBarButtonItemStyleBordered
                                                                       target:nil
                                                                       action:nil];
                                       [[self navigationItem] setBackBarButtonItem:newBackButton];
                                       
                                       vc.jokeList = itemsForView;
                                       vc.isQuery = YES;
                                       vc.topicString = [NSString stringWithFormat:@"Topic: %@",login.text];
                                       
                                       
                                       
                                       [self.navigationController pushViewController:vc animated:YES];
                                       
                                   }else{
                                       
                                       UIAlertController *alertController = [UIAlertController
                                                                             alertControllerWithTitle:@"Sorry!"
                                                                             message:[NSString stringWithFormat:@"We could not find any jokes about %@",login.text]
                                                                             preferredStyle:UIAlertControllerStyleAlert];
                                       UIAlertAction *okAction = [UIAlertAction
                                                                  actionWithTitle:NSLocalizedString(@"OK", @"OK action")
                                                                  style:UIAlertActionStyleDefault
                                                                  handler:^(UIAlertAction *action)
                                                                  {
                                                                      NSLog(@"OK action");
                                                                  }];
                                       
                                       [alertController addAction:okAction];
                                       [self presentViewController:alertController animated:YES completion:nil];

                                   }
                               }];
    [alertController addAction:okAction];
    [alertController addAction:cancelAction];
    
    
    [self presentViewController:alertController animated:YES completion:nil];
}

- (IBAction)randomClick:(id)sender {
    
            
    //        NSLog(@"%@",[rows objectAtIndex:0]);
            int rndValue = 1 + arc4random() % ([[[MyManager sharedManager] rawInput] count] - 1);
            NSArray *jokeLine = (NSArray*)[[[MyManager sharedManager] rawInput] objectAtIndex:rndValue];
            NSString *jokeString = [jokeLine objectAtIndex:1];
//    UIAlertController *alertController = [UIAlertController
//                                          alertControllerWithTitle:[NSString stringWithFormat:@"Random Joke"]
//                                          message:jokeString
//                                          preferredStyle:UIAlertControllerStyleAlert];
//    UIAlertAction *okAction = [UIAlertAction
//                               actionWithTitle:NSLocalizedString(@"OK", @"OK action")
//                               style:UIAlertActionStyleDefault
//                               handler:^(UIAlertAction *action)
//                               {
//                                   NSLog(@"OK action");
//                               }];
//    
//    [alertController addAction:okAction];
//    [self presentViewController:alertController animated:YES completion:nil];
    
    UIStoryboard *sb = [UIStoryboard storyboardWithName:@"Main" bundle:nil];
    JokeShowCaseViewController *vc = (JokeShowCaseViewController *)[sb instantiateViewControllerWithIdentifier:@"showcase"];
    vc.jokeString = (NSString *)jokeString;
    
    vc.scoreText = @"Score: 32.45";
    vc.sourceText = @"Source: Reddit";
    
    UIBarButtonItem *newBackButton =
    [[UIBarButtonItem alloc] initWithTitle:@""
                                     style:UIBarButtonItemStylePlain
                                    target:nil
                                    action:nil];
    [[self navigationItem] setBackBarButtonItem:newBackButton];
    self.navigationController.navigationBar.tintColor = [UIColor blackColor];
    
    [self.navigationController pushViewController:vc animated:YES];
    
    

}

- (IBAction)topJokesPressed:(id)sender {
    JokeListTableViewController *vc = [self.storyboard instantiateViewControllerWithIdentifier:@"topJokeVC"];
    
    NSArray *itemsForView = [[[MyManager sharedManager] rawInput] subarrayWithRange: NSMakeRange( 1, 11 )];
//    for (id thing in itemsForView){
//        NSArray *tmp = (NSArray*)thing;
//        NSString *jokeString = [tmp objectAtIndex:1];
//        jokeString = [jokeString stringByReplacingOccurrencesOfString:@" |||" withString:@"."];
//    }
    UIBarButtonItem *newBackButton =
    [[UIBarButtonItem alloc] initWithTitle:@""
                                     style:UIBarButtonItemStyleBordered
                                    target:nil
                                    action:nil];
    [[self navigationItem] setBackBarButtonItem:newBackButton];
    
    vc.jokeList = itemsForView;
    vc.isQuery = NO;
    

    
    [self.navigationController pushViewController:vc animated:YES];
    
}

- (IBAction)composeButtonPressed:(id)sender {
    //TODO 
    UIAlertController *alertController = [UIAlertController
                                          alertControllerWithTitle:@"Enter a Joke"
                                          message:@"and we will add it to the Joke database!"
                                          preferredStyle:UIAlertControllerStyleAlert];
    
    [alertController addTextFieldWithConfigurationHandler:^(UITextField *textField)
     {
         textField.placeholder = NSLocalizedString(@"Enter joke here", @"Login");
     }];
    
    UIAlertAction *cancelAction = [UIAlertAction
                                   actionWithTitle:NSLocalizedString(@"Cancel", @"Cancel action")
                                   style:UIAlertActionStyleCancel
                                   handler:^(UIAlertAction *action)
                                   {
                                       NSLog(@"Cancel action");
                                   }];
    
    UIAlertAction *okAction = [UIAlertAction
                               actionWithTitle:NSLocalizedString(@"Submit", @"OK action")
                               style:UIAlertActionStyleDefault
                               handler:^(UIAlertAction *action)
                               {
                                   UITextField *login = alertController.textFields.firstObject;
                                   NSString *actualJoke = login.text;
                                   if (actualJoke.length > 0){
                                       MHTextIndex * index = [[MyManager sharedManager] sharedIndex];
                                       [index indexObject:actualJoke];
                                       self.index = index;
                                   }
                               
                               }];
    [alertController addAction:cancelAction];
    [alertController addAction:okAction];
     [self presentViewController:alertController animated:YES completion:nil];
    
}

@end

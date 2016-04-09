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
    [NSTimer scheduledTimerWithTimeInterval:0.05f target:self selector:@selector(someMethod) userInfo:nil repeats:YES];
    
    
   
    
    [self.navigationController.navigationBar setTitleTextAttributes:
     @{NSForegroundColorAttributeName:[UIColor blackColor],NSFontAttributeName:[UIFont fontWithName:@"AvenirNext-Regular" size:20.0f]}];
    
    
    
        // Do any additional setup after loading the view, typically from a nib.
}
- (void)someMethod
{
    
    self.view.backgroundColor = [UIColor colorWithRed:_x green:_y blue:_z alpha:1.0f];
    
    CGFloat xFloat = [self randomFloatBetween:.001 and:.02];
    CGFloat yFloat = [self randomFloatBetween:.001 and:.02];
    CGFloat zFloat = [self randomFloatBetween:.001 and:.02];
    
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
    
    UIAlertAction *okAction = [UIAlertAction
                               actionWithTitle:NSLocalizedString(@"OK", @"OK action")
                               style:UIAlertActionStyleDefault
                               handler:^(UIAlertAction *action)
                               {
                                   UITextField *login = alertController.textFields.firstObject;
                                   NSArray* result = [self.index searchResultForKeyword:login.text options:NSEnumerationConcurrent];
                                   
                                   if ([result count] >0){
                                       MHSearchResultItem *top = result[0];
                                       NSLog(@"%@",top.context[@"title"]);
                                   }
                               }];
    [alertController addAction:okAction];
    
    
    [self presentViewController:alertController animated:YES completion:nil];
}
@end

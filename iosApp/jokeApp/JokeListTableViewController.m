//
//  JokeListTableViewController.m
//  jokeApp
//
//  Created by Patrick Wilson on 4/10/16.
//  Copyright © 2016 Patrick Wilson. All rights reserved.
//

#import "JokeListTableViewController.h"
#import "JokeShowCaseViewController.h"
#import "JokeTableViewCell.h"
#define ARC4RANDOM_MAX      0x100000000

@interface JokeListTableViewController ()

@end

@implementation JokeListTableViewController

- (void)viewDidLoad {
    [super viewDidLoad];
//    self.jokeList = [NSArray new];
    self.navigationController.navigationBar.tintColor = [UIColor blackColor];
    
    if (self.isQuery){
        self.navigationItem.title = self.topicString;
    }
    
    // Uncomment the following line to preserve selection between presentations.
    // self.clearsSelectionOnViewWillAppear = NO;
    
    // Uncomment the following line to display an Edit button in the navigation bar for this view controller.
    // self.navigationItem.rightBarButtonItem = self.editButtonItem;
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

#pragma mark - Table view data source

- (NSInteger)numberOfSectionsInTableView:(UITableView *)tableView {
    return 1;
}

- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section {
    return [self.jokeList count];
}


- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath {
//    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:@"test"];
//    
////    cell.selectionStyle = UITableViewCellSelectionStyleNone;
//
//    
//    if (cell == nil){
//        cell = [[UITableViewCell alloc] initWithStyle:UITableViewCellStyleDefault reuseIdentifier:@"test"];
//    }
    
    
    JokeTableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:@"myCell"];
    
    NSArray *jokeLine = (NSArray*)[self.jokeList objectAtIndex:indexPath.row];
    NSString *jokeString =[jokeLine objectAtIndex:1];
    jokeString = [jokeString stringByReplacingOccurrencesOfString:@" |||" withString:@" - "];
    cell.mainLabel.text = jokeString;
    double val = ((double)arc4random() / ARC4RANDOM_MAX);
    float tmpScore = 98.7 - indexPath.row - val;
    cell.scoreLabel.text = [NSString stringWithFormat:@"Score: %.02f",tmpScore];
    cell.sourceLabel.text = @"Source: Reddit";
    return cell;
}

-(CGFloat)tableView:(UITableView *)tableView heightForRowAtIndexPath:(NSIndexPath *)indexPath {
    return  130.0;
    
    
    
    
}

- (void)tableView:(UITableView *)tableView didSelectRowAtIndexPath:(NSIndexPath *)indexPath{
    [self.tableView deselectRowAtIndexPath:[self.tableView indexPathForSelectedRow] animated:YES];
    
    UIStoryboard *sb = [UIStoryboard storyboardWithName:@"Main" bundle:nil];
    JokeShowCaseViewController *vc = (JokeShowCaseViewController *)[sb instantiateViewControllerWithIdentifier:@"showcase"];
    NSArray *jokeLine = (NSArray*)[self.jokeList objectAtIndex:indexPath.row];
    vc.jokeString = (NSString *)[jokeLine objectAtIndex:1];
    
    JokeTableViewCell *cell = [tableView cellForRowAtIndexPath:indexPath];
    vc.scoreText = cell.scoreLabel.text;
    vc.sourceText = cell.sourceLabel.text;
    
    UIBarButtonItem *newBackButton =
    [[UIBarButtonItem alloc] initWithTitle:@""
                                     style:UIBarButtonItemStylePlain
                                    target:nil
                                    action:nil];
    [[self navigationItem] setBackBarButtonItem:newBackButton];
    [self.navigationController pushViewController:vc animated:YES];
    
    

}



/*
// Override to support conditional editing of the table view.
- (BOOL)tableView:(UITableView *)tableView canEditRowAtIndexPath:(NSIndexPath *)indexPath {
    // Return NO if you do not want the specified item to be editable.
    return YES;
}
*/

/*
// Override to support editing the table view.
- (void)tableView:(UITableView *)tableView commitEditingStyle:(UITableViewCellEditingStyle)editingStyle forRowAtIndexPath:(NSIndexPath *)indexPath {
    if (editingStyle == UITableViewCellEditingStyleDelete) {
        // Delete the row from the data source
        [tableView deleteRowsAtIndexPaths:@[indexPath] withRowAnimation:UITableViewRowAnimationFade];
    } else if (editingStyle == UITableViewCellEditingStyleInsert) {
        // Create a new instance of the appropriate class, insert it into the array, and add a new row to the table view
    }   
}
*/

/*
// Override to support rearranging the table view.
- (void)tableView:(UITableView *)tableView moveRowAtIndexPath:(NSIndexPath *)fromIndexPath toIndexPath:(NSIndexPath *)toIndexPath {
}
*/

/*
// Override to support conditional rearranging of the table view.
- (BOOL)tableView:(UITableView *)tableView canMoveRowAtIndexPath:(NSIndexPath *)indexPath {
    // Return NO if you do not want the item to be re-orderable.
    return YES;
}
*/

/*
#pragma mark - Navigation

// In a storyboard-based application, you will often want to do a little preparation before navigation
- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender {
    // Get the new view controller using [segue destinationViewController].
    // Pass the selected object to the new view controller.
}
*/

@end

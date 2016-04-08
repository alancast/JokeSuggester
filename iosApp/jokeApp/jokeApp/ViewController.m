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
@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    self.index = [[MyManager sharedManager] sharedIndex];
    
    
        // Do any additional setup after loading the view, typically from a nib.
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (IBAction)pressed:(id)sender {
    NSArray* result = [self.index searchResultForKeyword:@"chill" options:NSEnumerationConcurrent];
    MHSearchResultItem *top = result[0];
    NSLog(@"%@",top.context[@"title"]);
}
@end

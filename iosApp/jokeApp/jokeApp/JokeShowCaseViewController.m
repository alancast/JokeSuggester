//
//  JokeShowCaseViewController.m
//  jokeApp
//
//  Created by Patrick Wilson on 4/10/16.
//  Copyright © 2016 Patrick Wilson. All rights reserved.
//

#import "JokeShowCaseViewController.h"

@interface JokeShowCaseViewController ()

@end

@implementation JokeShowCaseViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    self.jokeString = [self.jokeString stringByReplacingOccurrencesOfString:@" |||" withString:@" - "];
    self.mainLabel.text = self.jokeString;
    self.sourceLabel.text = self.sourceText;
    self.scoreLabel.text = self.scoreText;
    // Do any additional setup after loading the view.
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

/*
#pragma mark - Navigation

// In a storyboard-based application, you will often want to do a little preparation before navigation
- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender {
    // Get the new view controller using [segue destinationViewController].
    // Pass the selected object to the new view controller.
}
*/

@end

//
//  JokeShowCaseViewController.h
//  jokeApp
//
//  Created by Patrick Wilson on 4/10/16.
//  Copyright © 2016 Patrick Wilson. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface JokeShowCaseViewController : UIViewController
@property (strong, nonatomic) IBOutlet UILabel *mainLabel;
@property (strong, nonatomic) NSString *jokeString;
@property (strong, nonatomic) IBOutlet UILabel *scoreLabel;
@property (strong, nonatomic) IBOutlet UILabel *sourceLabel;
@property (nonatomic, strong) NSString *sourceText;
@property (nonatomic, strong) NSString *scoreText;


@end

//
//  JokeTableViewCell.h
//  jokeApp
//
//  Created by Patrick Wilson on 4/10/16.
//  Copyright © 2016 Patrick Wilson. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface JokeTableViewCell : UITableViewCell
@property (strong, nonatomic) IBOutlet UILabel *mainLabel;
@property (strong, nonatomic) IBOutlet UILabel *scoreLabel;
@property (strong, nonatomic) IBOutlet UILabel *sourceLabel;

@end

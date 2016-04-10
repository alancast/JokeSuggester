//
//  JokeListTableViewController.h
//  jokeApp
//
//  Created by Patrick Wilson on 4/10/16.
//  Copyright © 2016 Patrick Wilson. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface JokeListTableViewController : UITableViewController

@property (strong, nonatomic) NSArray *jokeList;
@property ( nonatomic) BOOL isQuery;
@property (nonatomic,strong) NSString *topicString;

@end

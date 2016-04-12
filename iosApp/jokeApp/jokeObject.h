//
//  jokeObject.h
//  jokeApp
//
//  Created by Patrick Wilson on 4/11/16.
//  Copyright © 2016 Patrick Wilson. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface jokeObject : NSObject

@property (strong, nonatomic) NSString *jokeBody;
@property (strong, nonatomic) NSString *author;
@property (nonatomic, strong) NSNumber *idNum;
@property (nonatomic, strong) NSNumber *weightNum;

- initWithJoke:(NSString *)jokeBody byAuthor:(NSString *)author andID:(NSNumber *)idNum andWeight:(NSNumber *)weightNum;




@end

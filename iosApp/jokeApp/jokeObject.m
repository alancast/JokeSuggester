//
//  jokeObject.m
//  jokeApp
//
//  Created by Patrick Wilson on 4/11/16.
//  Copyright © 2016 Patrick Wilson. All rights reserved.
//

#import "jokeObject.h"

@implementation jokeObject

- (id)initWithJoke:(NSString *)jokeBody byAuthor:(NSString *)author andID:(NSNumber *)idNum andWeight:(NSNumber *)weightNum{
    
    if ((self = [super init])) {
        self.jokeBody = jokeBody;
        self.author = author;
        self.idNum = idNum;
        self.weightNum = weightNum;
    }
    
    return self;
}



@end

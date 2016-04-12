//
//  MyManager.m
//  jokeApp
//
//  Created by Patrick Wilson on 4/8/16.
//  Copyright © 2016 Patrick Wilson. All rights reserved.
//

#import "MyManager.h"
#import "CHCSVParser.h"
#import "jokeObject.h"

@implementation MyManager

@synthesize sharedIndex, rawInput;

#pragma mark Singleton Methods


+ (id)sharedManager {
    static MyManager *sharedMyManager = nil;
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        sharedMyManager = [[self alloc] init];
    });
    return sharedMyManager;
}

- (id)init {
    if (self = [super init]) {
        rawInput = [NSMutableArray new];
        sharedIndex = [MHTextIndex textIndexInLibraryWithName:@"my.awesome.index"];
        
        [sharedIndex setIdentifier:^NSData *(jokeObject *myJoke){
            return [NSKeyedArchiver archivedDataWithRootObject:myJoke.idNum];
        }];
        
        [sharedIndex setIndexer:^MHIndexedObject *(jokeObject *object, NSData *identifier){
            MHIndexedObject *indx = [MHIndexedObject new];
            indx.strings = @[ object.jokeBody]; // Indexed strings
            indx.weight = [object.weightNum floatValue];                // Weight given to this object, when sorting results
            indx.context = @{@"title": object.jokeBody,@"author":object.author,@"score":object.weightNum};             // A NSDictionary that will be given alongside search results
            return indx;
        }];
//
        
//        NSLog(@"%@",[rows objectAtIndex:0]);
        
        
//        NSURL *url = [[NSBundle mainBundle] URLForResource:@"bestEver" withExtension:@"csv"];
//        NSError *error = nil;
//        NSArray *rows = [NSArray arrayWithContentsOfCSVURL:url];
//        if (rows == nil) {
//            //something went wrong; log the error and exit
//            NSLog(@"error parsing file: %@", error);
//        }
//        rawInput = rows;
        

        [self takeInMasterList];
        [self takeInRandomList];
        [self takeInTopJokes];
        
        
    }
    return self;
}

- (void)takeInMasterList{
    
    NSURL *url = [[NSBundle mainBundle] URLForResource:@"masterList" withExtension:@"csv"];
    NSError *error = nil;
    NSArray *rows = [NSArray arrayWithContentsOfCSVURL:url];
    if (rows == nil) {
        //something went wrong; log the error and exit
        NSLog(@"error parsing file: %@", error);
    }
    
    for (id line in rows){
        NSArray *jokeLine = (NSArray*)line;
        NSString *jokeString = [jokeLine objectAtIndex:1];
        NSString *authorString = [jokeLine objectAtIndex:2];
        NSNumber *idString = [jokeLine objectAtIndex:0];
        jokeObject *Test = [[jokeObject alloc] initWithJoke:jokeString byAuthor:authorString andID:idString andWeight:[NSNumber numberWithInt:1]];
        
        [sharedIndex indexObject:Test];
    }
}
- (void)takeInRandomList{
    NSURL *url = [[NSBundle mainBundle] URLForResource:@"randomJokes" withExtension:@"csv"];
    NSError *error = nil;
    NSArray *rows = [NSArray arrayWithContentsOfCSVURL:url];
    if (rows == nil) {
        //something went wrong; log the error and exit
        NSLog(@"error parsing file: %@", error);
    }
    
    for (id line in rows){
        NSArray *jokeLine = (NSArray*)line;
        NSString *jokeString = [jokeLine objectAtIndex:1];
        NSString *authorString = [jokeLine objectAtIndex:0];
        NSNumber *weight = [NSNumber numberWithFloat:32.3];
        jokeObject *test = [[jokeObject alloc] initWithJoke:jokeString byAuthor:authorString andID:[NSNumber numberWithFloat:1.0] andWeight:weight];
        [rawInput addObject:test];
    }

}

-(void)takeInTopJokes{
    
    
}


- (void)dealloc {
    // Should never be called, but just here for clarity really.
}

@end

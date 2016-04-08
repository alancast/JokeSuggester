//
//  MyManager.m
//  jokeApp
//
//  Created by Patrick Wilson on 4/8/16.
//  Copyright © 2016 Patrick Wilson. All rights reserved.
//

#import "MyManager.h"

@implementation MyManager

@synthesize sharedIndex;

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
        sharedIndex = [MHTextIndex textIndexInLibraryWithName:@"my.awesome.index"];
        
        [sharedIndex setIdentifier:^NSData *(NSString *myString){
            return [myString dataUsingEncoding:NSUTF8StringEncoding]; // a NSData instance
        }];
        
        [sharedIndex setIndexer:^MHIndexedObject *(NSString *object, NSData *identifier){
            MHIndexedObject *indx = [MHIndexedObject new];
            indx.strings = @[ object]; // Indexed strings
            indx.weight = 1;                // Weight given to this object, when sorting results
            indx.context = @{@"title": object};             // A NSDictionary that will be given alongside search results
            return indx;
        }];
        
        [sharedIndex indexObject:@"this is a test"];
        [sharedIndex indexObject:@"this is another test"];
        [sharedIndex indexObject:@"Patrick"];
        [sharedIndex indexObject:@"ok chill"];
        [sharedIndex indexObject:@"what is this"];
    }
    return self;
}

- (void)dealloc {
    // Should never be called, but just here for clarity really.
}

@end

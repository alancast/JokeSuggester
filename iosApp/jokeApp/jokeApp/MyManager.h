//
//  MyManager.h
//  jokeApp
//
//  Created by Patrick Wilson on 4/8/16.
//  Copyright © 2016 Patrick Wilson. All rights reserved.
//

#import <Foundation/Foundation.h>
#import <UIKit/UIKit.h>

#import <MHTextSearch/MHTextIndex.h>
#import <MHTextSearch/MHTextSearch.h>


@interface MyManager : NSObject {
    MHTextIndex *sharedIndex;
}

@property (nonatomic, retain) MHTextIndex *sharedIndex;

+ (id)sharedManager;

@end

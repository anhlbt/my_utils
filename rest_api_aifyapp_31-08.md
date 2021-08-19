REST API DESCRIPTTION

===
## Management API

### Create account

__Curl URL__
> curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{"email": "demo%40aifyapp.com", "password": "demo1234"}' 'http://localhost:3003/api/Accounts'

__Respond body__
```
{
  "email": "demo@aifyapp.com",
  "device_token": []
}
```

### Login

__Curl URL__
> curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{"email": "demo%40aifyapp.com", "password": "demo1234"}' 'http://localhost:3003/api/Accounts/login'

__Respond body__
```
{
  "id": "NQiFakxJbEvIYUwQZXg3JoHw6xzoE6FSLop77q79goDybDimjXJcgdpQKVFDlPGh",
  "ttl": 1209600,
  "created": "2018-08-13T04:24:54.562Z",
  "userId": "demo@aifyapp.com"
}
```

### Logout

__Curl URL__
> curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' 'http://localhost:3003/api/Accounts/logout?access_token=NQiFakxJbEvIYUwQZXg3JoHw6xzoE6FSLop77q79goDybDimjXJcgdpQKVFDlPGh'

__Respond body__
```
```

### Add social user

__Curl URL__
> curl -X POST --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' -d 'socialId=2034529026816383&username=LE%20Mac%20Sau&accessToken=EAACLXTuiZBKkBAIaLZCHFzuwC9FK83ZCt7RTNnY1pRmc5qrIKCabMe4v8LWGZBaVpdsZBf83YvaLMmZAU6D27uCoibCxyTfywgg1rbGhqbojacQvEXO8c32imoLOZCpcZCA5RaYctiSZAjmGZCXGaZAGOU8yZBXJ7S45kWK63ZAfDjVk7OgZDZD' 'http://localhost:3003/api/Accounts/demo%40aifyapp.com/addFacebookUser?access_token=ahpQTjkhd0ftw7OlfWMzKmI7TmHCCzSdXT9jYBmDOCGgUCrbBSX41Wl7AijvW8zq'

__Respond body__
```
```

### List social user

__Curl URL__
> curl -X GET --header 'Accept: application/json' 'http://localhost:3003/api/Accounts/nctam%40atvn.com/listUsers?access_token=CD5obaDL8VU3BUProhDK3E9eX3QWKXuDzgnzfV9M5IlQCeXEVSPt05drTlB3EN2I'

__Respond body__
```
[
  {
    "id": "df865410-90ab-11e8-91fd-1904e54b34fa",
    "external_id": "110392633096780",
    "username": "huongarrive",
    "fullname": null,
    "avatar_url": null,
    "social_type": "facebook",
    "access_token": "EAACLXTuiZBKkBAJZBxOEcwblSFcFfnr13bzq5soAWUsKIqxx7hGRvSPFPbPg2J7GrirqhHy4bnylZCZCZAyWh6MdRvx9imTSxS4K7yNJrZCHxHhRCz1mTAPCrZAQ9QZC9NvxWsL66vm8uV65CAu0DMuH3QZB7xf0kY5qTKFip0ioPtBZB0F2fZBiyCbd4DZBE8bhkMgZD",
    "created": "2018-07-26T08:14:09.000Z",
    "updated": "2018-07-26T08:14:09.000Z",
    "account_id": "nctam@atvn.com"
  },
  {
    "id": "e35bed20-90ab-11e8-91fd-1904e54b34fa",
    "external_id": "17841406553883197",
    "username": "arrivetechnologiesvietnam",
    "fullname": "Arrive Technologies",
    "avatar_url": "https://scontent.xx.fbcdn.net/v/t51.2885-15/26072303_527685310939693_978597591040131072_n.jpg?_nc_cat=0&oh=cd1445d33a18daac781c842617b0780d&oe=5C12A73B",
    "social_type": "instagram_business",
    "access_token": "EAACLXTuiZBKkBAGm9OVwhI5ZAmHdYyIPhCQDbH9X6RMzBc1ukBmsBi0TZCQRxpynsv5DXeJffOMoGved8jJT5gHWTZCxTuDQQtrgRZC3XnrTotBkkoBzOztRGB7yn588wJpDOKntFbf9geLLWNTMJv6fZCNTZCbxR5upxTZAGLxFZB9leGxAJ3UVEarMSgDcqO1IZD",
    "created": "2018-07-26T08:14:16.000Z",
    "updated": "2018-07-26T08:14:16.000Z",
    "account_id": "nctam@atvn.com"
  },
  {
    "id": "e296c860-90ab-11e8-91fd-1904e54b34fa",
    "external_id": "17841407517779759",
    "username": "vnbeachhotel",
    "fullname": null,
    "avatar_url": "https://scontent.xx.fbcdn.net/v/t51.2885-15/30593611_597162827301678_7047393617308024832_n.jpg?_nc_cat=0&oh=0efe2d9168efcc3d865cd62cb36b3da1&oe=5BE044EF",
    "social_type": "instagram_business",
    "access_token": "EAACLXTuiZBKkBACCtdNNPN7ZBOZCXMYTGVN0p7OEZCoqn4Bh0ZBmNodxDFfAZBFZAi35QOyum3jgcZBIpUlvly3nnoyatdXIgDwDUU4Miig7lU80gEntNN9hdE0k0fZCMD8EtYZCdT9T8fHYLbDGZCPJ8RQCZBmE3USsow9JjSl3X7YsTNM7KqOHN8XMjIXBsdkk3fwZD",
    "created": "2018-07-26T08:14:15.000Z",
    "updated": "2018-07-26T08:14:15.000Z",
    "account_id": "nctam@atvn.com"
  }
]
```

### removeFacebookUser

__Curl URL__
> curl -X POST --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' -d 'socialId=2034529026816383' 'http://localhost:3003/api/Accounts/demo%40aifyapp.com/removeFacebookUser?access_token=ahpQTjkhd0ftw7OlfWMzKmI7TmHCCzSdXT9jYBmDOCGgUCrbBSX41Wl7AijvW8zq'

__Respond body__
```

```

## Statistics API

### overviewInfoOverall

__Curl URL__
> curl -X GET --header 'Accept: application/json' 'http://localhost:3003/api/SocialUsers/overviewInfoOverall?social_type=instagram_business&social_id=17841406553883197&from=1533686400&until=1534324690&access_token=SGWmfCWcb3hwubFF5EEHREwfamIRemaGnmEVELa2nHmMDqb25MVQ1wOfXFkEUGS6'

__Respond body__
```
{
  "total_followers": 2736441,
  "followers_evolution": 4569,
  "total_followings": 444,
  "total_posts": 4391,
  "impressions": 221.6681216837561,
  "impressions_growth": 0,
  "reaches": null,
  "reaches_growth": null,
  "engagement_rate": 11.664804316674495,
  "engagement_rate_growth": 0
}
```

### recentMediasHistories

__Curl URL__
> curl -X GET --header 'Accept: application/json' 'http://localhost:3003/api/SocialUsers/recentMediasHistories?social_type=instagram_business&social_id=17841406553883197&from=1533686400&until=1534324690&access_token=SGWmfCWcb3hwubFF5EEHREwfamIRemaGnmEVELa2nHmMDqb25MVQ1wOfXFkEUGS6'

__Respond body__
```
[
  {
    "created": "2018-08-08T07:00:00+07:00",
    "post_url": "http://url.com",
    "comment_cnt": 2,
    "like_cnt": 63
  },
  {
    "created": "2018-08-09T07:00:00+07:00",
    "post_url": "http://url.com",
    "comment_cnt": 0,
    "like_cnt": 51
  },
  {
    "created": "2018-08-10T07:00:00+07:00",
    "post_url": "http://url.com",
    "comment_cnt": 15,
    "like_cnt": 34
  },
  {
    "created": "2018-08-11T07:00:00+07:00",
    "post_url": "http://url.com",
    "comment_cnt": 6,
    "like_cnt": 11
  },
  {
    "created": "2018-08-12T07:00:00+07:00",
    "post_url": "http://url.com",
    "comment_cnt": 9,
    "like_cnt": 32
  },
  {
    "created": "2018-08-13T07:00:00+07:00",
    "post_url": "http://url.com",
    "comment_cnt": 18,
    "like_cnt": 44
  },
  {
    "created": "2018-08-14T07:00:00+07:00",
    "post_url": "http://url.com",
    "comment_cnt": 11,
    "like_cnt": 13
  },
  {
    "created": "2018-08-15T07:00:00+07:00",
    "post_url": "http://url.com",
    "comment_cnt": 6,
    "like_cnt": 17
  }
]
```

### recentStoriesHistories

__Curl URL__
> curl -X GET --header 'Accept: application/json' 'http://localhost:3003/api/SocialUsers/recentStoriesHistories?social_type=instagram_business&social_id=17841406553883197&from=1533081600&until=1533969277&access_token=gQwMk3BHPWqADSB2HYi0gbERRNGwcXvlClYjDB8uSMA2eBGuZ0r7YXHQPtkmTAsA'

__Respond body__
```
[
  {
    "created": "2018-08-01T07:00:00+07:00",
    "story_url": "",
    "total_impression": 2,
    "total_reach": 90
  },
  {
    "created": "2018-08-02T07:00:00+07:00",
    "story_url": "",
    "total_impression": 67,
    "total_reach": 94
  },
  {
    "created": "2018-08-03T07:00:00+07:00",
    "story_url": "",
    "total_impression": 73,
    "total_reach": 25
  },
  {
    "created": "2018-08-04T07:00:00+07:00",
    "story_url": "",
    "total_impression": 1,
    "total_reach": 25
  },
  {
    "created": "2018-08-05T07:00:00+07:00",
    "story_url": "",
    "total_impression": 59,
    "total_reach": 77
  },
  {
    "created": "2018-08-06T07:00:00+07:00",
    "story_url": "",
    "total_impression": 88,
    "total_reach": 46
  },
  {
    "created": "2018-08-07T07:00:00+07:00",
    "story_url": "",
    "total_impression": 63,
    "total_reach": 99
  },
  {
    "created": "2018-08-08T07:00:00+07:00",
    "story_url": "",
    "total_impression": 95,
    "total_reach": 6
  },
  {
    "created": "2018-08-09T07:00:00+07:00",
    "story_url": "",
    "total_impression": 19,
    "total_reach": 96
  },
  {
    "created": "2018-08-10T07:00:00+07:00",
    "story_url": "",
    "total_impression": 11,
    "total_reach": 15
  },
  {
    "created": "2018-08-11T07:00:00+07:00",
    "story_url": "",
    "total_impression": 14,
    "total_reach": 46
  }
]
```
### followerGrowthHistories

__Curl URL__
> curl -X GET --header 'Accept: application/json' 'http://localhost:3003/api/SocialUsers/followerGrowthHistories?social_type=instagram_business&social_id=17841406553883197&from=1533686400&until=1534324690&access_token=SGWmfCWcb3hwubFF5EEHREwfamIRemaGnmEVELa2nHmMDqb25MVQ1wOfXFkEUGS6'

__Respond body__
```
[
  {
    "day": "2018-08-08T07:00:00+07:00",
    "follower_grow": 15,
    "new_followers_cnt": 1
  },
  {
    "day": "2018-08-09T07:00:00+07:00",
    "follower_grow": 96,
    "new_followers_cnt": 15
  },
  {
    "day": "2018-08-10T07:00:00+07:00",
    "follower_grow": 5,
    "new_followers_cnt": 74
  },
  {
    "day": "2018-08-11T07:00:00+07:00",
    "follower_grow": 76,
    "new_followers_cnt": 50
  },
  {
    "day": "2018-08-12T07:00:00+07:00",
    "follower_grow": 68,
    "new_followers_cnt": 31
  },
  {
    "day": "2018-08-13T07:00:00+07:00",
    "follower_grow": 58,
    "new_followers_cnt": 62
  },
  {
    "day": "2018-08-14T07:00:00+07:00",
    "follower_grow": 39,
    "new_followers_cnt": 89
  },
  {
    "day": "2018-08-15T07:00:00+07:00",
    "follower_grow": 33,
    "new_followers_cnt": 93
  }
]
```

### followingGrowthHistories

__Curl URL__
> curl -X GET --header 'Accept: application/json' 'http://localhost:3003/api/SocialUsers/followingGrowthHistories?social_type=instagram_business&social_id=17841406553883197&from=1533686400&until=1534324690&access_token=SGWmfCWcb3hwubFF5EEHREwfamIRemaGnmEVELa2nHmMDqb25MVQ1wOfXFkEUGS6'

__Respond body__
```
[
  {
    "day": "2018-08-08T07:00:00+07:00",
    "follows_grow": 34
  },
  {
    "day": "2018-08-09T07:00:00+07:00",
    "follows_grow": 15
  },
  {
    "day": "2018-08-10T07:00:00+07:00",
    "follows_grow": 11
  },
  {
    "day": "2018-08-11T07:00:00+07:00",
    "follows_grow": 7
  },
  {
    "day": "2018-08-12T07:00:00+07:00",
    "follows_grow": 49
  },
  {
    "day": "2018-08-13T07:00:00+07:00",
    "follows_grow": 21
  },
  {
    "day": "2018-08-14T07:00:00+07:00",
    "follows_grow": 34
  },
  {
    "day": "2018-08-15T07:00:00+07:00",
    "follows_grow": 49
  }
]
```

### engagementRateHistories

__Curl URL__
> curl -X GET --header 'Accept: application/json' 'http://localhost:3003/api/SocialUsers/engagementRateHistories?social_type=instagram_business&social_id=17841406553883197&from=1533686400&until=1534324690&access_token=SGWmfCWcb3hwubFF5EEHREwfamIRemaGnmEVELa2nHmMDqb25MVQ1wOfXFkEUGS6'

__Respond body__
```
[
  {
    "day": "2018-08-08T07:00:00+07:00",
    "average_engagement_rate": 85.2596559888872
  },
  {
    "day": "2018-08-09T07:00:00+07:00",
    "average_engagement_rate": 44.67354352784996
  },
  {
    "day": "2018-08-10T07:00:00+07:00",
    "average_engagement_rate": 29.107462606614163
  },
  {
    "day": "2018-08-11T07:00:00+07:00",
    "average_engagement_rate": 48.23189982735045
  },
  {
    "day": "2018-08-12T07:00:00+07:00",
    "average_engagement_rate": 76.69574770013851
  },
  {
    "day": "2018-08-13T07:00:00+07:00",
    "average_engagement_rate": 24.259775942312988
  },
  {
    "day": "2018-08-14T07:00:00+07:00",
    "average_engagement_rate": 55.56198392121612
  },
  {
    "day": "2018-08-15T07:00:00+07:00",
    "average_engagement_rate": 69.17227171694842
  }
]
```

### engagement

__Curl URL__
> curl -X GET --header 'Accept: application/json' 'http://localhost:3003/api/SocialUsers/engagement?social_type=instagram_business&social_id=17841406553883197&from=1533686400&until=1534324690&access_token=SGWmfCWcb3hwubFF5EEHREwfamIRemaGnmEVELa2nHmMDqb25MVQ1wOfXFkEUGS6'

__Respond body__
```
{
  "total_medias": 16,
  "total_likes": 2,
  "total_comments": 54
}
```

### likeHistories

__Curl URL__
> curl -X GET --header 'Accept: application/json' 'http://localhost:3003/api/SocialUsers/likeHistories?social_type=instagram_business&social_id=17841406553883197&from=1533686400&until=1534324690&access_token=SGWmfCWcb3hwubFF5EEHREwfamIRemaGnmEVELa2nHmMDqb25MVQ1wOfXFkEUGS6'

__Respond body__
```
[
  {
    "date": "2018-08-08T07:00:00+07:00",
    "total_like_cnt": 2
  },
  {
    "date": "2018-08-09T07:00:00+07:00",
    "total_like_cnt": 195
  },
  {
    "date": "2018-08-10T07:00:00+07:00",
    "total_like_cnt": 194
  },
  {
    "date": "2018-08-11T07:00:00+07:00",
    "total_like_cnt": 108
  },
  {
    "date": "2018-08-12T07:00:00+07:00",
    "total_like_cnt": 111
  },
  {
    "date": "2018-08-13T07:00:00+07:00",
    "total_like_cnt": 200
  },
  {
    "date": "2018-08-14T07:00:00+07:00",
    "total_like_cnt": 148
  },
  {
    "date": "2018-08-15T07:00:00+07:00",
    "total_like_cnt": 2
  }
]
```

### commentHistories

__Curl URL__
> curl -X GET --header 'Accept: application/json' 'http://localhost:3003/api/SocialUsers/commentHistories?social_type=instagram_business&social_id=17841406553883197&from=1533686400&until=1534324690&access_token=SGWmfCWcb3hwubFF5EEHREwfamIRemaGnmEVELa2nHmMDqb25MVQ1wOfXFkEUGS6'

__Respond body__
```
[
  {
    "date": "2018-08-08T07:00:00+07:00",
    "total_comment_cnt": 14
  },
  {
    "date": "2018-08-09T07:00:00+07:00",
    "total_comment_cnt": 59
  },
  {
    "date": "2018-08-10T07:00:00+07:00",
    "total_comment_cnt": 132
  },
  {
    "date": "2018-08-11T07:00:00+07:00",
    "total_comment_cnt": 104
  },
  {
    "date": "2018-08-12T07:00:00+07:00",
    "total_comment_cnt": 117
  },
  {
    "date": "2018-08-13T07:00:00+07:00",
    "total_comment_cnt": 130
  },
  {
    "date": "2018-08-14T07:00:00+07:00",
    "total_comment_cnt": 44
  },
  {
    "date": "2018-08-15T07:00:00+07:00",
    "total_comment_cnt": 118
  }
]
```

### averageEngagement

__Curl URL__
> curl -X GET --header 'Accept: application/json' 'http://localhost:3003/api/SocialUsers/averageEngagement?social_type=instagram_business&social_id=17841406553883197&from=1533686400&until=1534324690&access_token=SGWmfCWcb3hwubFF5EEHREwfamIRemaGnmEVELa2nHmMDqb25MVQ1wOfXFkEUGS6'

__Respond body__
```
{
  "average_likes_growth": 11364.623161764706,
  "average_comments_growth": -14.53125,
  "average_engagement": 25608.529411764706,
  "average_engagement_growth": 11350.091911764706,
  "average_likes": 25406.529411764706,
  "average_comments": 202,
  "average_reach": 0,
  "new_inquiries": 0
}
```

### genderFollowers

__Curl URL__
> curl -X GET --header 'Accept: application/json' 'http://localhost:3003/api/SocialUsers/genderFollowers?social_type=instagram_business&social_id=17841406553883197&from=1533686400&until=1534324690&access_token=SGWmfCWcb3hwubFF5EEHREwfamIRemaGnmEVELa2nHmMDqb25MVQ1wOfXFkEUGS6'

__Respond body__
```
{
  "male": {
    "55-64": 13962,
    "25-34": 160632,
    "65+": 9304,
    "13-17": 12718,
    "18-24": 108909,
    "45-54": 39629,
    "total": 430249,
    "35-44": 85095
  },
  "female": {
    "35-44": 64103,
    "25-34": 110704,
    "65+": 7463,
    "13-17": 14724,
    "18-24": 83851,
    "45-54": 36312,
    "total": 330776,
    "55-64": 13619
  },
  "followers": 821929
}
```

### countriesFollowers

__Curl URL__
> curl -X GET --header 'Accept: application/json' 'http://localhost:3003/api/SocialUsers/countriesFollowers?social_type=instagram_business&social_id=17841406553883197&from=1533686400&until=1534324690&access_token=SGWmfCWcb3hwubFF5EEHREwfamIRemaGnmEVELa2nHmMDqb25MVQ1wOfXFkEUGS6'

__Respond body__
```
{
  "countries": {
    "FR": 12399,
    "DE": 14630,
    "JP": 3950,
    "DZ": 3692,
    "BR": 48425,
    "CO": 14769,
    "VE": 8889,
    "RU": 11713,
    "NL": 4392,
    "PT": 3814,
    "TW": 2878,
    "TR": 19699,
    "NG": 2975,
    "TH": 7584,
    "PE": 3479,
    "PK": 5921,
    "PH": 6790,
    "EG": 12830,
    "PL": 3425,
    "CH": 2901,
    "AE": 5519,
    "GR": 2922,
    "CN": 3008,
    "CL": 10000,
    "IQ": 8150,
    "CA": 20141,
    "IR": 21145,
    "IT": 24159,
    "EC": 3571,
    "ZA": 7001,
    "AR": 10854,
    "AU": 15666,
    "IL": 3839,
    "IN": 38339,
    "TZ": 3192,
    "ID": 25595,
    "ES": 15604,
    "MA": 5370,
    "US": 156256,
    "KW": 2834,
    "SA": 12549,
    "MY": 10433,
    "MX": 27421,
    "SE": 4409,
    "GB": 28180
  },
  "followers": 821929
}
```

### citiesFollowers

__Curl URL__
> curl -X GET --header 'Accept: application/json' 'http://localhost:3003/api/SocialUsers/citiesFollowers?social_type=instagram_business&social_id=17841406553883197&from=1533686400&until=1534324690&access_token=SGWmfCWcb3hwubFF5EEHREwfamIRemaGnmEVELa2nHmMDqb25MVQ1wOfXFkEUGS6'

__Respond body__
```
{
  "cities": {
    "Baghdad, Baghdad Governorate": 2887,
    "Barcelona, CataluÃ±a": 1774,
    "Houston, Texas": 1998,
    "Caracas, Capital District": 2617,
    "Alexandria, Alexandria Governorate": 1869,
    "Dubai, Dubai": 3145,
    "Pune, Maharashtra": 1820,
    "Buenos Aires, Ciudad AutÃ³noma de Buenos Aires": 2836,
    "Moscow, Moscow": 3356,
    "New York, New York": 7144,
    "Istanbul, Istanbul Province": 7532,
    "Paris, ÃŽle-de-France": 2471,
    "Sydney, New South Wales": 3395,
    "Tehran, Tehran Province": 10226,
    "Toronto, Ontario": 2821,
    "Dar es Salaam, Dar es Salaam": 1678,
    "Bangalore, Karnataka": 2206,
    "Cairo, Cairo Governorate": 5808,
    "Lima, Lima Region": 2311,
    "Singapore, Central Region": 2530,
    "Mumbai, Maharashtra": 4473,
    "MedellÃ­n, Antioquia": 2101,
    "Rio de Janeiro, Rio de Janeiro (state)": 2976,
    "Delhi, Delhi": 1702,
    "BogotÃ¡, Distrito Especial": 4970,
    "SÃ£o Paulo, SÃ£o Paulo (state)": 6353,
    "Chicago, Illinois": 2190,
    "Rome, Lazio": 2117,
    "Mexico City, Distrito Federal": 6664,
    "Madrid, Comunidad de Madrid": 2061,
    "Bangkok, Bangkok": 4464,
    "London, England": 6146,
    "Jeddah, Makkah Region": 3035,
    "Melbourne, Victoria": 2999,
    "Miami, Florida": 2214,
    "Jakarta, Jakarta": 5812,
    "Hong Kong, Hong Kong": 1967,
    "Milan, Lombardia": 1694,
    "Kuala Lumpur, Kuala Lumpur": 2697,
    "Santiago, Santiago Metropolitan Region": 5167,
    "Atlanta, Georgia": 1655,
    "Los Angeles, California": 4211,
    "Amman, Amman Governorate": 2117,
    "Riyadh, Riyadh Region": 4852,
    "Baku, Baku": 1930
  },
  "followers": 821929
}
```

### postsHistories

__Curl URL__
> curl -X GET --header 'Accept: application/json' 'http://localhost:3003/api/SocialUsers/postsHistories?social_type=instagram_business&social_id=17841406553883197&from=1533686400&until=1534324690&access_token=SGWmfCWcb3hwubFF5EEHREwfamIRemaGnmEVELa2nHmMDqb25MVQ1wOfXFkEUGS6'

__Respond body__
```
[
  {
    "total_post_cnt": 4403,
    "day": "2018-08-22T07:00:00.000Z"
  },
  {
    "total_post_cnt": 4403,
    "day": "2018-08-21T07:00:00.000Z"
  },
  {
    "total_post_cnt": 4403,
    "day": "2018-08-20T07:00:00.000Z"
  },
  {
    "total_post_cnt": 4403,
    "day": "2018-08-19T07:00:00.000Z"
  },
  {
    "total_post_cnt": 4403,
    "day": "2018-08-18T07:00:00.000Z"
  },
  {
    "total_post_cnt": 4403,
    "day": "2018-08-17T07:00:00.000Z"
  },
  {
    "total_post_cnt": 4402,
    "day": "2018-08-16T07:00:00.000Z"
  },
  {
    "total_post_cnt": 4400,
    "day": "2018-08-15T07:00:00.000Z"
  },
  {
    "total_post_cnt": 4399,
    "day": "2018-08-14T07:00:00.000Z"
  },
  {
    "total_post_cnt": 4398,
    "day": "2018-08-13T07:00:00.000Z"
  },
  {
    "total_post_cnt": 4396,
    "day": "2018-08-12T07:00:00.000Z"
  },
  {
    "total_post_cnt": 4393,
    "day": "2018-08-11T07:00:00.000Z"
  },
  {
    "total_post_cnt": 4391,
    "day": "2018-08-10T07:00:00.000Z"
  }
]
```

### postDistribution

__Curl URL__
> curl -X GET --header 'Accept: application/json' 'http://localhost:3003/api/SocialUsers/postDistribution?social_type=instagram_business&social_id=17841406553883197&access_token=SGWmfCWcb3hwubFF5EEHREwfamIRemaGnmEVELa2nHmMDqb25MVQ1wOfXFkEUGS6'

__Respond body__
```
{
  "2018-06-03T17:00:00.000Z": null,
  "2018-06-10T17:00:00.000Z": null,
  "2018-06-17T17:00:00.000Z": null,
  "2018-06-24T17:00:00.000Z": null,
  "2018-07-01T17:00:00.000Z": null,
  "2018-07-08T17:00:00.000Z": null,
  "2018-07-15T17:00:00.000Z": null,
  "2018-07-22T17:00:00.000Z": null,
  "2018-07-29T17:00:00.000Z": 0,
  "2018-08-05T17:00:00.000Z": 0,
  "2018-08-12T17:00:00.000Z": 0,
  "2018-08-19T17:00:00.000Z": 0
}
```

### bestTimePosting

__Curl URL__
> curl -X GET --header 'Accept: application/json' 'http://localhost:3003/api/SocialUsers/bestTimePosting?social_type=instagram_business&social_id=17841406553883197&access_token=gQwMk3BHPWqADSB2HYi0gbERRNGwcXvlClYjDB8uSMA2eBGuZ0r7YXHQPtkmTAsA'

__Respond body__
```
[
  {
    "date": "Wednesday",
    "engagement": {
      "14": 28,
      "15": 3,
      "17": 12,
      "20": 157
    }
  },
  {
    "date": "Thursday",
    "engagement": {
      "15": 186,
      "18": 168,
      "23": 31
    }
  },
  {
    "date": "Friday",
    "engagement": {
      "6": 105,
      "10": 123,
      "11": 96,
      "12": 43,
      "15": 52,
      "19": 27,
      "20": 2
    }
  },
  {
    "date": "Saturday",
    "engagement": {
      "14": 104,
      "17": 120,
      "21": 104
    }
  },
  {
    "date": "Sunday",
    "engagement": {
      "4": 45,
      "8": 24,
      "10": 113,
      "11": 1,
      "15": 84,
      "19": 109,
      "20": 84
    }
  },
  {
    "date": "Monday",
    "engagement": {
      "7": 11,
      "11": 92,
      "16": 97,
      "19": 161,
      "23": 118
    }
  },
  {
    "date": "Tuesday",
    "engagement": {
      "6": 181,
      "11": 135,
      "16": 97,
      "18": 9,
      "23": 43
    }
  }
]
```

### hashtagPerformmance

__Curl URL__
> curl -X GET --header 'Accept: application/json' 'http://localhost:3003/api/SocialUsers/hashtagPerformmance?social_type=instagram_business&social_id=17841406553883197&access_token=gQwMk3BHPWqADSB2HYi0gbERRNGwcXvlClYjDB8uSMA2eBGuZ0r7YXHQPtkmTAsA'

__Respond body__
```
[
  {
    "hashtag": "travel",
    "engagement": 9
  },
  {
    "hashtag": "passion",
    "engagement": 6
  },
  {
    "hashtag": "luxury",
    "engagement": 8
  }
]
```

### followerOnlineHabit

__Curl URL__
> curl -X GET --header 'Accept: application/json' 'http://localhost:3003/api/SocialUsers/followerOnlineHabit?social_type=instagram_business&social_id=17841406553883197&access_token=gQwMk3BHPWqADSB2HYi0gbERRNGwcXvlClYjDB8uSMA2eBGuZ0r7YXHQPtkmTAsA'

__Respond body__
```
[
  {
    "day": "Thursday",
    "online_followers": {},
    "followers": 831506
  },
  {
    "day": "Wednesday",
    "online_followers": {},
    "followers": 831636
  },
  {
    "day": "Tuesday",
    "online_followers": {
      "0": 79064,
      "1": 81776,
      "2": 91529,
      "3": 106537,
      "4": 119540,
      "5": 127310,
      "6": 131915,
      "7": 135536,
      "8": 138046,
      "9": 140356,
      "10": 139441,
      "11": 138592,
      "12": 139078,
      "13": 135758,
      "14": 127653,
      "15": 115174,
      "16": 105015,
      "17": 101476,
      "18": 100602,
      "19": 98469,
      "20": 91553,
      "21": 84669,
      "22": 80188,
      "23": 75136
    },
    "followers": 831761
  },
  {
    "day": "Monday",
    "online_followers": {
      "0": 79396,
      "1": 83147,
      "2": 92746,
      "3": 106727,
      "4": 119373,
      "5": 128062,
      "6": 133165,
      "7": 136642,
      "8": 140412,
      "9": 141744,
      "10": 139985,
      "11": 140441,
      "12": 140484,
      "13": 137027,
      "14": 128913,
      "15": 115849,
      "16": 106057,
      "17": 102296,
      "18": 101427,
      "19": 98452,
      "20": 91723,
      "21": 84789,
      "22": 80181,
      "23": 74643
    },
    "followers": 831512
  },
  {
    "day": "Sunday",
    "online_followers": {
      "0": 84788,
      "1": 86633,
      "2": 89906,
      "3": 95583,
      "4": 105209,
      "5": 116913,
      "6": 128470,
      "7": 137253,
      "8": 141676,
      "9": 144002,
      "10": 144233,
      "11": 143407,
      "12": 141645,
      "13": 137358,
      "14": 129882,
      "15": 118384,
      "16": 108303,
      "17": 103930,
      "18": 102176,
      "19": 98136,
      "20": 91035,
      "21": 84869,
      "22": 80196,
      "23": 74531
    },
    "followers": 831198
  },
  {
    "day": "Saturday",
    "online_followers": {
      "0": 83378,
      "1": 85332,
      "2": 88826,
      "3": 96807,
      "4": 107974,
      "5": 119788,
      "6": 129116,
      "7": 135290,
      "8": 139333,
      "9": 140925,
      "10": 140847,
      "11": 139194,
      "12": 136500,
      "13": 132856,
      "14": 127147,
      "15": 118347,
      "16": 108202,
      "17": 101975,
      "18": 98664,
      "19": 96976,
      "20": 93048,
      "21": 86925,
      "22": 82130,
      "23": 78468
    },
    "followers": 830965
  },
  {
    "day": "Friday",
    "online_followers": {
      "0": 80045,
      "1": 82867,
      "2": 91374,
      "3": 104565,
      "4": 118700,
      "5": 126728,
      "6": 132069,
      "7": 136313,
      "8": 138648,
      "9": 139292,
      "10": 138024,
      "11": 136289,
      "12": 135541,
      "13": 133632,
      "14": 128247,
      "15": 118220,
      "16": 108259,
      "17": 101405,
      "18": 98381,
      "19": 95863,
      "20": 91274,
      "21": 84789,
      "22": 80458,
      "23": 77434
    },
    "followers": 830727
  }
]
```

### profileViewHistories

__Curl URL__
> curl -X GET --header 'Accept: application/json' 'http://localhost:3003/api/SocialUsers/profileViewHistories?social_type=instagram_business&social_id=17841406553883197&from=1533686400&until=1534324690&access_token=SGWmfCWcb3hwubFF5EEHREwfamIRemaGnmEVELa2nHmMDqb25MVQ1wOfXFkEUGS6'

__Respond body__
```
[
  {
    "day": "2018-08-08T07:00:00+07:00",
    "profile_views_cnt": 90
  },
  {
    "day": "2018-08-09T07:00:00+07:00",
    "profile_views_cnt": 78
  },
  {
    "day": "2018-08-10T07:00:00+07:00",
    "profile_views_cnt": 41
  },
  {
    "day": "2018-08-11T07:00:00+07:00",
    "profile_views_cnt": 23
  },
  {
    "day": "2018-08-12T07:00:00+07:00",
    "profile_views_cnt": 40
  },
  {
    "day": "2018-08-13T07:00:00+07:00",
    "profile_views_cnt": 0
  },
  {
    "day": "2018-08-14T07:00:00+07:00",
    "profile_views_cnt": 40
  },
  {
    "day": "2018-08-15T07:00:00+07:00",
    "profile_views_cnt": 0
  }
]
```

### websiteClickHistories

__Curl URL__
> curl -X GET --header 'Accept: application/json' 'http://localhost:3003/api/SocialUsers/websiteClickHistories?social_type=instagram_business&social_id=17841406553883197&from=1533686400&until=1534324690&access_token=SGWmfCWcb3hwubFF5EEHREwfamIRemaGnmEVELa2nHmMDqb25MVQ1wOfXFkEUGS6'

__Respond body__
```
[
  {
    "day": "2018-08-08T07:00:00+07:00",
    "website_clicks_cnt": 14
  },
  {
    "day": "2018-08-09T07:00:00+07:00",
    "website_clicks_cnt": 20
  },
  {
    "day": "2018-08-10T07:00:00+07:00",
    "website_clicks_cnt": 74
  },
  {
    "day": "2018-08-11T07:00:00+07:00",
    "website_clicks_cnt": 90
  },
  {
    "day": "2018-08-12T07:00:00+07:00",
    "website_clicks_cnt": 38
  },
  {
    "day": "2018-08-13T07:00:00+07:00",
    "website_clicks_cnt": 61
  },
  {
    "day": "2018-08-14T07:00:00+07:00",
    "website_clicks_cnt": 73
  },
  {
    "day": "2018-08-15T07:00:00+07:00",
    "website_clicks_cnt": 34
  }
]
```

### emailClickHistories

__Curl URL__
> curl -X GET --header 'Accept: application/json' 'http://localhost:3003/api/SocialUsers/emailClickHistories?social_type=instagram_business&social_id=17841406553883197&from=1533686400&until=1534324690&access_token=SGWmfCWcb3hwubFF5EEHREwfamIRemaGnmEVELa2nHmMDqb25MVQ1wOfXFkEUGS6'

__Respond body__
```
[
  {
    "day": "2018-08-08T07:00:00+07:00",
    "email_clicks_cnt": 65
  },
  {
    "day": "2018-08-09T07:00:00+07:00",
    "email_clicks_cnt": 88
  },
  {
    "day": "2018-08-10T07:00:00+07:00",
    "email_clicks_cnt": 68
  },
  {
    "day": "2018-08-11T07:00:00+07:00",
    "email_clicks_cnt": 17
  },
  {
    "day": "2018-08-12T07:00:00+07:00",
    "email_clicks_cnt": 76
  },
  {
    "day": "2018-08-13T07:00:00+07:00",
    "email_clicks_cnt": 79
  },
  {
    "day": "2018-08-14T07:00:00+07:00",
    "email_clicks_cnt": 62
  },
  {
    "day": "2018-08-15T07:00:00+07:00",
    "email_clicks_cnt": 95
  }
]
```

### directionClickHistories

__Curl URL__
> curl -X GET --header 'Accept: application/json' 'http://localhost:3003/api/SocialUsers/directionClickHistories?social_type=instagram_business&social_id=17841406553883197&from=1533686400&until=1534324690&access_token=SGWmfCWcb3hwubFF5EEHREwfamIRemaGnmEVELa2nHmMDqb25MVQ1wOfXFkEUGS6'

__Respond body__
```
[
  {
    "day": "2018-08-08T07:00:00+07:00",
    "directions_clicks": 47
  },
  {
    "day": "2018-08-09T07:00:00+07:00",
    "directions_clicks": 91
  },
  {
    "day": "2018-08-10T07:00:00+07:00",
    "directions_clicks": 79
  },
  {
    "day": "2018-08-11T07:00:00+07:00",
    "directions_clicks": 67
  },
  {
    "day": "2018-08-12T07:00:00+07:00",
    "directions_clicks": 85
  },
  {
    "day": "2018-08-13T07:00:00+07:00",
    "directions_clicks": 9
  },
  {
    "day": "2018-08-14T07:00:00+07:00",
    "directions_clicks": 90
  },
  {
    "day": "2018-08-15T07:00:00+07:00",
    "directions_clicks": 21
  }
]
```

### lastProfileActivities

__Curl URL__
> curl -X GET --header 'Accept: application/json' 'http://localhost:3003/api/SocialUsers/lastProfileActivities?social_type=instagram_business&social_id=17841406553883197&from=1533081600&until=1533969277&access_token=SGWmfCWcb3hwubFF5EEHREwfamIRemaGnmEVELa2nHmMDqb25MVQ1wOfXFkEUGS6'

__Respond body__
```
{
  "profile_views": 55,
  "website_clicks": 1,
  "email_clicks": 93,
  "get_directions_clicks": 55,
  "profile_views_growth": -25.454545454545453,
  "website_clicks_growth": -8000,
  "email_clicks_growth": 70.96774193548387,
  "get_directions_clicks_growth": -27.27272727272727
}
```

### getPostsWeeksDashBoard

__Curl URL__
> curl -X GET --header 'Accept: application/json' 'http://localhost:3003/api/AllPostsWeeksStatistics/getPostsWeeksDashBoard?owner_id=6af7f410-a13a-11e8-ae95-05512692b162&access_token=uHzrrI6F4wYbE8EdAf8prI2DvFeAfCl2XxKsmWNUnTC6O271cgSUk2xl5DEZwq4B'

__Respond body__
```
[
  {
    "impr": 0,
    "impr_post_cnt": 79,
    "start_day": "2018-08-13 00:00:00",
    "impr_changes_snapshot": [
      3.020515289308081,
      3.220669134485103,
      3.325017305152279,
      3.354659584816568,
      0.4633720932757686,
      0,
      0
    ],
    "score_changes_snapshot": [
      0.16000014229220796,
      0.16509039784673848,
      0.16858069334236073,
      0.17027744519387072,
      0.03300269215616479,
      0,
      0
    ],
    "impr_change": 13.384233407037799,
    "score_change": 0.6969513708313424,
    "imprs_snapshot": [
      94.69990687099074,
      97.92057600547585,
      101.24559331062815,
      104.60025289544474,
      0,
      0,
      0
    ],
    "score": 0,
    "post_cnt": 87,
    "end_day": "2018-08-19 00:00:00",
    "scores_snapshot": [
      3.774438143808902,
      3.939528541655641,
      4.108109234998001,
      4.278386680191875,
      0,
      0,
      0
    ]
  },
  {
    "impr": 38.71896634760386,
    "impr_post_cnt": 88,
    "start_day": "2018-08-06 00:00:00",
    "impr_changes_snapshot": [
      0.7022219493910766,
      0.7701847390815458,
      0.8254463227653753,
      0.91998476050935,
      1.027949029497436,
      1.0831603016893678,
      1.2023845620724407
    ],
    "score_changes_snapshot": [
      0.03582876993835252,
      0.03957383161648571,
      0.04277070766415045,
      0.048066690957101525,
      0.053688301405945923,
      0.05682508317162179,
      0.06392773816320392
    ],
    "impr_change": 6.531331665006587,
    "score_change": 0.3406811229168616,
    "imprs_snapshot": [
      32.88985663198834,
      33.66004137106988,
      34.48548769383526,
      35.405472454344604,
      36.43342148384205,
      37.51658178553141,
      38.71896634760386
    ],
    "score": 38.71896634760386,
    "post_cnt": 103,
    "end_day": "2018-08-12 00:00:00",
    "scores_snapshot": [
      1.221633599118347,
      1.2612074307348324,
      1.303978138398983,
      1.3520448293560854,
      1.4057331307620304,
      1.4625582139336528,
      1.526485952096857
    ]
  },
  {
    "impr": 33.82986094191344,
    "impr_post_cnt": 84,
    "start_day": "2018-07-30 00:00:00",
    "impr_changes_snapshot": [
      0.550718670766163,
      0.5556374640413078,
      0.5725266061916426,
      0.5928392578383692,
      0.6154748871826383,
      0.6534008213558546,
      0.6840945320461311
    ],
    "score_changes_snapshot": [
      0.025504282801934133,
      0.02642377950674656,
      0.027919797707787262,
      0.029075043967108312,
      0.03056775726785213,
      0.032529766410748666,
      0.03461589292034907
    ],
    "impr_change": 4.224692239422106,
    "score_change": 0.20663632058252615,
    "imprs_snapshot": [
      30.155887373257507,
      30.711524837298814,
      31.28405144349046,
      31.87689070132883,
      32.49236558851147,
      33.14576640986732,
      33.82986094191344
    ],
    "score": 33.82986094191344,
    "post_cnt": 98,
    "end_day": "2018-08-05 00:00:00",
    "scores_snapshot": [
      1.0651730377861361,
      1.091596817292883,
      1.1195166150006703,
      1.1485916589677787,
      1.1791594162356307,
      1.2116891826463794,
      1.2463050755667289
    ]
  },
  {
    "impr": 29.306126594385375,
    "impr_post_cnt": 90,
    "start_day": "2018-07-23 00:00:00",
    "impr_changes_snapshot": [
      0.6071093091592911,
      0.6059297453619835,
      0.5891050580404459,
      0.5661284638758768,
      0.5621459366144581,
      0.5566701433809774,
      0.5540383893308982
    ],
    "score_changes_snapshot": [
      0.021951882193964673,
      0.022370272927616827,
      0.022466964443821402,
      0.02246769144770264,
      0.023338642097425092,
      0.024211410256850658,
      0.02487480129847982
    ],
    "impr_change": 4.041127045763931,
    "score_change": 0.16168166466586117,
    "imprs_snapshot": [
      25.872108857780745,
      26.47803860314273,
      27.06714366118317,
      27.633272125059047,
      28.195418061673504,
      28.75208820505448,
      29.306126594385375
    ],
    "score": 29.306126594385375,
    "post_cnt": 99,
    "end_day": "2018-07-29 00:00:00",
    "scores_snapshot": [
      0.8894372679165058,
      0.9118075408441227,
      0.9342745052879441,
      0.9567421967356465,
      0.9800808388330717,
      1.0042922490899224,
      1.029167050388402
    ]
  }
]
```

### getPostsMonthsDashBoard

__Curl URL__
> curl -X GET --header 'Accept: application/json' 'http://localhost:3003/api/AllPostsWeeksStatistics/getPostsMonthsDashBoard?owner_id=6af7f410-a13a-11e8-ae95-05512692b162&access_token=uHzrrI6F4wYbE8EdAf8prI2DvFeAfCl2XxKsmWNUnTC6O271cgSUk2xl5DEZwq4B'

__Respond body__
```
[
  {
    "impr": 444.24229940820516,
    "impr_post_cnt": 228,
    "start_day": "2018-07-30 00:00:00",
    "impr_changes_snapshot": [
      7.263505955497658,
      11.802230903432957,
      10.413127813171787,
      0
    ],
    "score_changes_snapshot": [
      0.3552688321122008,
      0.6156167659725745,
      0.5340778951574943,
      0
    ],
    "impr_change": 29.47886467210243,
    "score_change": 1.5049634932422686,
    "imprs_snapshot": [
      378.3533480897709,
      444.24229940820516,
      343.1391932972419,
      0
    ],
    "score": 444.24229940820516,
    "post_cnt": 228,
    "end_day": "2018-08-26 00:00:00",
    "scores_snapshot": [
      13.666951435043527,
      17.033369481018546,
      13.942551422544252,
      0
    ]
  },
  {
    "impr": 125.33742813907408,
    "impr_post_cnt": 143,
    "start_day": "2018-07-02 00:00:00",
    "impr_changes_snapshot": [
      2.8689968049815167,
      2.817178847262282,
      2.780702736128181,
      2.6671438502041944
    ],
    "score_changes_snapshot": [
      0.09176030703845715,
      0.09001207353520667,
      0.09342841017391763,
      0.10670989867946837
    ],
    "impr_change": 11.134022238576176,
    "score_change": 0.38191068942705,
    "imprs_snapshot": [
      66.63816184774873,
      86.60358559404732,
      106.15940425230748,
      125.33742813907408
    ],
    "score": 125.33742813907408,
    "post_cnt": 150,
    "end_day": "2018-09-23 00:00:00",
    "scores_snapshot": [
      2.374317497389465,
      3.011685718621253,
      3.6481166064789226,
      4.35207748174725
    ]
  },
  {
    "impr": 64.66567005339606,
    "impr_post_cnt": 110,
    "start_day": "2018-06-04 00:00:00",
    "impr_changes_snapshot": [
      1.393434162592128,
      2.1689215328171643,
      2.8380800052867725,
      3.380260088910032
    ],
    "score_changes_snapshot": [
      0.05099117982533694,
      0.08141302073765845,
      0.10632758914844195,
      0.11805826932473094
    ],
    "impr_change": 9.780695789606092,
    "score_change": 0.3567900590361685,
    "imprs_snapshot": [
      12.048494684847359,
      24.770018374477836,
      42.95528539000822,
      64.66567005339606
    ],
    "score": 64.66567005339606,
    "post_cnt": 110,
    "end_day": "2018-10-21 00:00:00",
    "scores_snapshot": [
      0.42975275016026343,
      0.9033870183896904,
      1.5876075572707753,
      2.3773711754120597
    ]
  }
]
```

## Recommendation APIs

### recommendInfluencer

__Curl URL__
> curl -X POST --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' -d 'owner_id=a6145ff0-9ec1-11e8-a812-8fefaee9f9a9' 'http://localhost:3003/api/UserHashtagSettings/{id}/recommendInfluencer?access_token=uPk9TLYhgbkjT4qDKTZDjd4tUsD82kgsYG7d1lGNK6vazViBOJwdQInBSv2xyRu3'

__Respond body__
```
[
  {
    "username": "SAM BONNOR",
    "avatar_url": "",
    "link": "https://instagram.com/sambonnor",
    "followers": "26.6k",
    "location": "Australia",
    "gender": "",
    "age": null,
    "website": "",
    "post_count": 0,
    "like_count": 530,
    "engagement": "2.0%",
    "bio": ""
  },
  {
    "username": "Lo",
    "avatar_url": "",
    "link": "https://instagram.com/lorenpiretra",
    "followers": "6.2k",
    "location": "Santa Monica, California",
    "gender": "Female",
    "age": null,
    "website": "http://lorenpiretra.com",
    "post_count": 0,
    "like_count": 192,
    "engagement": "3.2%",
    "bio": "Los Angeles based creative - specializing in photography, story-telling, styling, and content creation."
  }
]
```

### recommendBrand

__Curl URL__
> curl -X POST --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' -d 'owner_id=a6145ff0-9ec1-11e8-a812-8fefaee9f9a9' 'http://localhost:3003/api/UserHashtagSettings/{id}/recommendBrand?access_token=uPk9TLYhgbkjT4qDKTZDjd4tUsD82kgsYG7d1lGNK6vazViBOJwdQInBSv2xyRu3'

__Respond body__
```
[
  {
    "username": "SAM BONNOR",
    "avatar_url": "",
    "link": "https://instagram.com/sambonnor",
    "followers": "26.6k",
    "location": "Australia",
    "gender": "",
    "age": null,
    "website": "",
    "post_count": 0,
    "like_count": 530,
    "engagement": "2.0%",
    "bio": ""
  },
  {
    "username": "Lo",
    "avatar_url": "",
    "link": "https://instagram.com/lorenpiretra",
    "followers": "6.2k",
    "location": "Santa Monica, California",
    "gender": "Female",
    "age": null,
    "website": "http://lorenpiretra.com",
    "post_count": 0,
    "like_count": 192,
    "engagement": "3.2%",
    "bio": "Los Angeles based creative - specializing in photography, story-telling, styling, and content creation."
  }
]
```

## Hashtag APIs

### searchHashtag

__Curl URL__
> curl -X GET --header 'Accept: application/json' 'http://localhost:3003/api/Accounts/nctam%40atvn.com/searchHashtag?textSearch=t&access_token=Xib5Tni5ZOBZHHbPjo1KL1Cpk3bPXLzmuJWWuo9c6tgLqRxsR5KNfTm0wBjEhmD6'


__Respond body__
```
[
  "travel",
  "hotel",
  "passion"
]
```

### addWatchLists

__Curl URL__
> curl -X POST --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' -d 'username=sofia' 'http://localhost:3003/api/Accounts/nctam%40atvn.com/addWatchLists?access_token=Xib5Tni5ZOBZHHbPjo1KL1Cpk3bPXLzmuJWWuo9c6tgLqRxsR5KNfTm0wBjEhmD6'


__Respond body__
```
{
  "username": "sofia",
  "avatar_url": "",
  "link": "",
  "followers": 0,
  "location": "",
  "gender": "",
  "age": 0,
  "website": "",
  "post_count": 0,
  "like_count": 0,
  "engagement": 0,
  "bio": ""
}
```

### removeWatchLists

__Curl URL__
> curl -X POST --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' -d 'username=sofia' 'http://localhost:3003/api/Accounts/nctam%40atvn.com/removeWatchLists?access_token=Xib5Tni5ZOBZHHbPjo1KL1Cpk3bPXLzmuJWWuo9c6tgLqRxsR5KNfTm0wBjEhmD6'


__Respond body__
```
```

### getWatchLists

__Curl URL__
>curl -X GET --header 'Accept: application/json' 'http://localhost:3003/api/Accounts/nctam%40atvn.com/getWatchLists?limit=5&access_token=Xib5Tni5ZOBZHHbPjo1KL1Cpk3bPXLzmuJWWuo9c6tgLqRxsR5KNfTm0wBjEhmD6'


__Respond body__
```
[
  {
    "username": "",
    "avatar_url": "",
    "link": "",
    "followers": 0,
    "location": "",
    "gender": "",
    "age": 0,
    "website": "",
    "post_count": 0,
    "like_count": 0,
    "engagement": 0,
    "bio": ""
  }
]
```

## Comment APIs

### newInquiries

__Curl URL__
>

__Respond body__
```
```

### existInquiries

__Curl URL__
>

__Respond body__
```
```

### newPositiveComments

__Curl URL__
>

__Respond body__
```
```

### existPositiveComments

__Curl URL__
>

__Respond body__
```
```

### newNegativeComments

__Curl URL__
>

__Respond body__
```
```

### existNegativeComments

__Curl URL__
>

__Respond body__
```
```

### updateNewInquiries

__Curl URL__
>

__Respond body__
```
```

### updateNewPositiveComments

__Curl URL__
>

__Respond body__
```
```

### updateNewNegativeComments

__Curl URL__
>

__Respond body__
```
```


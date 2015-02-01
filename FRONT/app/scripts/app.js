'use strict';

/**
 * @ngdoc overview
 * @name stockPredictApp
 * @description
 * # stockPredictApp
 *
 * Main module of the application.
 */
var baseServiceUrl = 'localhost:8000/';

var spapp = angular
  .module('stockPredictApp', [
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize'
  ]);

spapp.config(function ($routeProvider, $httpProvider) {
    $httpProvider.defaults.withCredentials = true;
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl'
      })
      .when('/about', {
        templateUrl: 'views/about.html',
        controller: 'AboutCtrl'
      })
      .when('/predict', {
        templateUrl: 'views/predict.html',
        controller: 'PredictCtrl'
      })
      .when('/test', {
        templateUrl: 'views/test.html'
      })
      .when('/space', {
        templateUrl: 'views/space.html',
        controller: 'SpaceCtrl'
      })
      .when('/statistics', {
        templateUrl: 'views/statistics.html',
        controller: 'StatCtrl'
      })
      .when('/follow', {
        templateUrl: 'views/follow.html',
        controller: 'FollowCtrl'
      })
      .otherwise({
        templateUrl: '404.html'
      });
  });

//service.config(function($resourceProvider) {
//  $resourceProvider.defaults.stripTrailingSlashes = true;
//});

'use strict';

/**
 * @ngdoc function
 * @name stockPredictApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the stockPredictApp
 */
var testHSP = [
  {
    "id": 1,
    "stockShortName": "ibm",
    "description": "this is IBM ",
    "created": "2014-12-27T11:12:04Z"
  },
  {
    "id": 2,
    "stockShortName": "BABA",
    "description": "this is BABA ",
    "created": "2014-12-31T12:13:56Z"
  },
  {
    "id": 3,
    "stockShortName": "ZNE",
    "description": "this is ZNE ",
    "created": "2014-12-31T12:14:04Z"
  },
  {
    "id": 4,
    "stockShortName": "TENC",
    "description": "this is TENC ",
    "created": "2014-12-31T12:14:11Z"
  },
  {
    "id": 5,
    "stockShortName": "ZADA",
    "description": "this is ZADA ",
    "created": "2014-12-31T12:14:17Z"
  },
  {
    "id": 6,
    "stockShortName": "LEVIS",
    "description": "this is LEVIS ",
    "created": "2014-12-31T12:14:23Z"
  }
]

angular.module('stockPredictApp')
  .controller('MainCtrl', function ($scope, $http) {
    $http.get('/hotStockInfo/').success(function(data, status, headers, config){
      $scope.hotStocks = testHSP;
    }).error(function (data, status, headers, config) {
      alert('Error');
    });
  });

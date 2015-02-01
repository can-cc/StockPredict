"use strict";
/**
 * Created by tyan on 14-12-28.
 */
var testSP = [
{
  "id": 2,
  "stockShortName": "BABA",
  "predict": 1.5,
  "predictExpTime": 10,
  "created": "2014-12-31T11:31:22Z"
}
];

angular.module('stockPredictApp')
  .controller('PredictCtrl', function ($scope, $http) {

    $http.get('/alive/').success(function (data, status, headers, config) {
      if(data == 0){
        $scope.logined = true;
      } else {
        $scope.logined = false;
      }
    }).error(function (data, status, headers, config) {
      alert('asking alive error');
    });


    $scope.predictClick = function (sName){
      $scope.rslShow = true;
      $scope.waitShow = true;
      $http.get('/stockPrediction/'+sName).success(function(data, status, headers, config){
        //$scope.error = data;
        if(data['Success'] == 'please wait!'){
          $('#myModal').modal();
        }else{$scope.predictions = [data];
          $scope.waitShow = false;
          $scope.predictionShow = true;
        }
      }).error(function (data, status, headers, config) {
        $scope.error = data;
      });
      //$scope.predictionShow = true;
      //$scope.rslShow = true;
      //$scope.predictions = testSP;
    };

    $scope.follow = function(stockShortName){
      if(stockShortName == null){
        alert("Do not modify the input box!");
      } else {
        $http.post('/userAddStock/',{stockShortName:stockShortName}).success(function(data, status, headers, config){

        }).error(function (data, status, headers, config) {

        });
      }

    };

  });

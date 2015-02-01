/**
 * Created by tyan on 15-2-1.
 */


angular.module('stockPredictApp')
  .controller('FollowCtrl', ['$scope', '$cookies', '$http', function ($scope, $cookie, $http) {
    $http.get('/userStock/').success(function(data, status, headers, config){
      $scope.follows = data;
    }).error(function (data, status, headers, config) {
      alert('Error');
    });

  }]);

/**
 * Created by tyan on 15-1-1.
 */
var testStat = {
  "stock": {
    "id": 88,
      "stockName": "Alibaba Group Holding Limited",
      "symbol": "BABA",
      "sector": "Consumer Services",
      "SE": "NYSE",
      "industry": "Catalog/Specialty Distribution\n"
  },
  "predict": -1.313354,
    "adjClose": 89.08,
    "predictExpTime": 10,
    "predictRst": 0,
    "timeOutAdjClose": null,
    "earnings": null
}


angular.module('stockPredictApp')
  .controller('StatCtrl', ['$scope', '$cookies', '$http', function ($scope, $cookie, $http) {
    $http.get('/spstat/').success(function(data, status, headers, config){
      $scope.stats = data['results'];
    }).error(function (data, status, headers, config) {
      alert('Error');
    });

  }]);

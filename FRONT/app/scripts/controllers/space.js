/**
 * Created by tyan on 14-12-31.
 */
"use strict";

var userProfile = {
  "user": {
    "id": 1,
    "username": "tyan",
    "first_name": "Tyan",
    "last_name": "Chan"
  },
  "nickName": "Tyan",
  "photo": null,
  "selfDescription": "Hello world!",
  "hometown": "Zhongshan",
  "nowCity": "Zhongshan"
};


angular.module('stockPredictApp')
  .controller('SpaceCtrl', ['$scope', '$cookies', '$http', function ($scope, $cookie, $http) {
    $http.get('/alive/').success(function (data, status, headers, config) {
      if(data == 0){
        $scope.loginShow = true;
      } else {
        showUserInfo(data);
        $scope.loginShow = false;
      }
    }).error(function (data, status, headers, config) {
      alert('asking alive error');
    });

    $scope.login = function(username, password){
      $scope.errorWarn = false;
      var req = {
        method: 'POST',
        url: '/api-auth/login/',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        },
        data: 'csrfmiddlewaretoken='+$cookie.csrftoken+'&username='+username+'&password='+password+'&submit=Log+in'
      };
      $http(req).success(function (data, status, headers, config) {
        loginVi();
      }).error(function (Sdata, status, headers, config) {
        loginVi();
      });
    };

    function showUserInfo(userId){
      $http.get('/userInfo/').success(function (data, status, headers, config) {
        $scope.userProfile = data;
      }).error(function (Sdata, status, headers, config) {
        alert('show userinfo error');
        alert(Sdata + status + headers);
      });
      $scope.userInfo = true;
    }

    function loginVi(){
      var id = alive();
      if(id == 0){
        $scope.errorWarn = true;
      }else{
        showUserInfo(id);
        $scope.loginShow = false;
      }
    }

    function alive(){
      $http.get('/alive/').success(function (data, status, headers, config) {
        return data;
      }).error(function (data, status, headers, config) {
        return 0;
      });
    }

   /* $http.get('/alive/').success(function (data, status, headers, config) {
      if(data != '0') {
        alert(data);
        $http.get('/userInfo/'+data).success(function (Sdata, status, headers, config) {
          alert(Sdata);
        }).error(function (Sdata, status, headers, config) {
          alert(Sdata + status + headers);
        });
      } else {
        $scope.loginShow = true;
      }
    }).error(function (data, status, headers, config) {
      alert(data + status + headers);
    });*/

   /* $scope.loginShow = true;
    $scope.login = function(username, password){
      $scope.errorWarn = false;
      var req = {
        method: 'POST',
        url: '/api-auth/login/',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        },
        data: 'csrfmiddlewaretoken='+$cookie.csrftoken+'&username='+username+'&password='+password+'&submit=Log+in'
      };
      $http(req).then(alert(alive()));
    };
*/

    /*alert('fuck');
    $http.get('/alive/').success(function (data, status, headers, config) {
      if(data != '0') {
        alert(data);
        $http.get('/userInfo/'+data).success(function (Sdata, status, headers, config) {
          alert(Sdata);
        }).error(function (Sdata, status, headers, config) {
          alert(Sdata + status + headers);
        });
      } else {
        $scope.loginShow = true;
      }
    }).error(function (data, status, headers, config) {
      alert(data + status + headers);
    });*/

  }]);



var app = angular.module('shippable', ['ngRoute']);

app.config(function ($routeProvider) {
    $routeProvider.
        when("/issue",
            {
                templateUrl: "issue/issue.html",
                controller: "ManageController"
            }
        ).
	    when("/result",
            {
                templateUrl: "result/result.html",
                controller: "ResultController"
            }
        ).otherwise(
        {
            templateUrl: "404.html",
            controller: "404Controller"
        }
        )
    }
)
app.controller('ManageController',['$scope','$http', function ($scope,$http) {
//    $scope.viewRooms = function(){
//        $http({
//                method: 'GET',
//                url: chimeroom.base_url + '/viewrooms',
//                data: null
//        }).then(
//            function (result) {
//                $scope.availableRooms = result.data
//                console.log($scope.availableRooms)
//
//            },
//            function (err) {
//                console.log(err)
//            });
//    }
//    $scope.viewRooms()

}]);
app.controller('ResultController',['$scope', '$http', function ($scope, $http) {


}]);

app.controller('404Controller', ['$scope', function ($scope) {
}]);

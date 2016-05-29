var app = angular.module('shippable', ['ngRoute']);

app.config(function ($routeProvider,$httpProvider) {
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
    $scope.viewResult = false
    $scope.showResult = function(formGetIssues){
        $scope.form_object = {};
        $scope.form_object["url"] = formGetIssues.url.$modelValue;

        // calling the api
        $http({
            method: 'POST',
            url: "http://127.0.0.1:8000/viewresult",
            data: $scope.form_object,
        }).then(
            function (result) {
                $scope.data = result.data
                $scope.viewResult = true
            },
            function (err) {
                console.log(err)
            });
    }

}]);


app.controller('404Controller', ['$scope', function ($scope) {
}]);

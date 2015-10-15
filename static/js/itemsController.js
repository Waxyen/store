var app = angular.module("app", ["xeditable", "ui.bootstrap"]);

app.run(['editableOptions', function(editableOptions) {
  editableOptions.theme = 'bs3';
}]);

app.controller("ItemsCtrl", ['$http', '$scope', function($http, $scope) {
    var app = this;

    $scope.currentPage = 1;
    $scope.maxSize = 7;
    $scope.url = window.location.href;
   
    $http.get("/getUserId").success(function (data) {
        $scope.userId = data;
    })
    
    $scope.refresh = function() {
        $http.get("/api/items?page="+$scope.currentPage).success(function (data) {
            $scope.items = data.objects;
            $scope.totalItems = data.num_results;
        })
    }
    
    $scope.refresh();
    
    $scope.add = function(item) {
        if($scope.item.name && $scope.item.price){
            $http.post("/api/items", {
                "name": $scope.item.name,
                "price": $scope.item.price,
                "user_id": $scope.userId
            }).success(function () {
                $scope.item.name = null;
                $scope.item.price = null;
                $scope.currentPage = Math.ceil(($scope.totalItems +1) / 10);
                $scope.refresh();
            })
        }
    }
    
    $scope.update = function(index) {
        $http.put("/api/items/"+$scope.items[index].id, {
            "name": $scope.items[index].name,
            "price": $scope.items[index].price
        }).then(function (data) {
            $scope.items[index] = data.data;
        })
    }
    
    $scope.delete = function(item) {
        if (confirm("Are you sure to delete item '"+ item.name +"'?")) {
            $http.delete("/api/items/"+item.id).success(function () {
                $scope.refresh();
            })
        }
    }
}])
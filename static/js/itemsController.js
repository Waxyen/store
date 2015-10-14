var app = angular.module("app", ["xeditable"]);

app.run(function(editableOptions) {
  editableOptions.theme = 'bs3';
});

app.controller("ItemsCtrl", function($http, $scope) {
    var app = this;
    
    $scope.user = {
        name: 'awesome user'
    }
    
    $scope.refresh = function() {
        $http.get("/api/items").success(function (data) {
            app.items = data.objects;
        })
    }
    
    $scope.refresh();
    
    $scope.add = function() {
        if($scope.item){
            if($scope.item.name && $scope.item.price){
                $http.post("/api/items", {
                    "name": $scope.item.name,
                    "price": $scope.item.price
                }).success(function () {
                    $scope.item.name = null;
                    $scope.item.price = null;
                    $scope.refresh();
                })
            }
        }
    }
    
    $scope.update = function(index) {
        $http.put("/api/items/"+app.items[index].id, {
            "name": app.items[index].name,
            "price": app.items[index].price
        }).success(function () {
            $scope.refresh();
        })
    }
    
    $scope.delete = function(item) {
        if (confirm("Are you sure to delete item '"+ item.name +"'?")) {
            $http.delete("/api/items/"+item.id).success(function () {
                $scope.refresh();
            })
        }
    }
})
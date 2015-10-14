var app = angular.module("app", []);

app.controller("SigninCtrl", function($scope) {
    var app = this;
	
	if(window.location.href.indexOf("error_wrong_email_or_password") > -1) {
		$scope.errorMessage = "Wrong e-mail or password, try again";
	} else if (window.location.href.indexOf("error_something_unknown_went_wrong") > -1) {
		$scope.errorMessage = "Something went terribly wrong, try again";
	} else if (window.location.href.indexOf("not_authorized") > -1) {
		$scope.errorMessage = "You are not authorized, log in first!";
	} else {
		$scope.errorMessage = null;
	}
})
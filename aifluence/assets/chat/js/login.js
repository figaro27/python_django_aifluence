'use strict';


function Login() {
    // this.isLoginPageRendered = false;
    this.isLogin = false;
    this.token = document.querySelector('#chat_session_token').value;
    // this.token = 'asdfsdf';
    this.userId = parseInt(document.querySelector('#chat_id').value.replace(/,/g, ''));
}

// Login.prototype.init = function(){
//     var self = this;

//     return new Promise(function(resolve, reject) {
//         var user = localStorage.getItem('user');
//         if(user && !app.user){
//             var savedUser = JSON.parse(user);
//             app.room = savedUser.tag_list;
//             self.login(savedUser)
//                 .then(function(){
//                     resolve(true);
//                 }).catch(function(error){
//                 reject(error);
//             });
//         } else {
//             resolve(false);
//         }
//     });
// };

Login.prototype.login = function () {
    var self = this;
        // if(self.isLoginPageRendered){
        // } else {
        //     // self.renderLoadingPage();
        // }
        return new Promise(function(resolve, reject) {
        QB.createSession(function(csErr, csRes) {
            var userRequiredParams = {
                'login':document.querySelector('#username_').value,
                'password': 'Asdfg@123#'
            };
            if (csErr) {
                loginError(csErr);
            } else {
                app.token = csRes.token;
                QB.login(userRequiredParams, function(loginErr, loginUser){
                    if(loginErr) {
                        /** Login failed, trying to create account */
                        QB.users.create(userRequiredParams, function (createErr, createUser) {
                            if (createErr) {
                                loginError(createErr);
                            } else {
                                QB.login(userRequiredParams, function (reloginErr, reloginUser) {
                                    if (reloginErr) {
                                        loginError(reloginErr);
                                    } else {
                                        loginSuccess(reloginUser);
                                    }
                                });login
                            }
                        });
                    } else {
                        /** Update info */
                        // if(loginUser.user_tags !== userRequiredParams.tag_list || loginUseloginr.full_name !== userRequiredParams.full_name) {
                        //     QB.users.update(loginUser.id, {
                        //         'full_name': userRequiredParams.full_name,
                        //         'tag_list': userRequiredParams.tag_list
                        //     }, function(updateError, updateUser) {
                        //         if(updateError) {
                        //             loginError(updateError);
                        //         } else {
                        //             loginSuccess(updateUser);
                        //         }
                        //     });
                        // } else {
                        //     loginSuccess(loginUser);
                        // }
                        loginSuccess(loginUser);
                    }
                });
            }
        });

        function loginSuccess(userData){
            app.user = userModule.addToCache(userData);
            app.user.user_tags = userData.user_tags;
            if (QB.chat.isConnected) {
                self.isLogin = true;
                resolve();
            } else {
                QB.chat.connect({userId: app.user.id, password: 'Asdfg@123#'}, function(err, roster){
                    if (err) {
                        console.error(err);
                        reject(err);
                    } else {
                        self.isLogin = true;
                        resolve();
                    }
                });
            }

        }

        function loginError(error){
            // self.renderLoginPage();
            console.error(error);
            var message = Object.keys(error.detail).map(function (key) {
                return key + ' ' + error.detail[key].join('')
            })
            alert(message);
            reject(error);
        }
    });

};

Login.prototype.renderLoadingPage = function() {
    helpers.clearView(app.page);
    app.page.innerHTML = helpers.fillTemplate('tpl_loading');
    var self = this;
    // this.isLoginPageRendered = true;
    var user = {
        id: this.userId,
        login: document.querySelector('#username_').value,
        password: 'Asdfg@123#',
        full_name: ""
    };
    localStorage.setItem('user', JSON.stringify(user));
    app.token = this.token;

    console.log('token renderloadingpage--------------------------' + this.token);

    app.user = userModule.addToCache(user);
    app.user.user_tags = user.user_tags;
    QB.setToken(this.token);

    return new Promise(function(resolve, reject) {
        if (!QB.chat.isConnected) {
            QB.chat.connect({userId: app.user.id, password: user.password}, function(err, roster){
                if (err) {
                    reject(err);
                } else {
                    self.isLogin = true;
                    resolve();
                }
            })
        }



    });
};

var loginModule = new Login();

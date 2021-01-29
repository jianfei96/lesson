var vm = new Vue({
    el: '#app',
    //{{}} => [[]]
    delimiters: ['[[',']]'],
    data: {
        error_username: false,
        error_username_message: '请输入5-12个字符用户名',
        username: '',
        error_password: false,
        error_password_message: '请输入5-12个字符密码',
        password: '',
    },
    methods: {
        check_username: function (){
            var re = /^[a-zA-Z0-9-_]{5,12}$/
            if (re.test(this.username)){
                this.error_username = false
            }else {
                this.error_username = true
            }
        },
        check_pwd: function () {
            var re = /^[a-zA-Z0-9-_]{5,12}$/
            if (re.test(this.password)){
                this.error_password = false
            }else {
                this.error_password = true
            }
        },
        on_submit:function () {
            this.check_username()
            this.check_pwd()
            if(this.error_name || this.error_password) {
                // 不满足条件
                window.event.returnValue = false
            }
        }
    }
})
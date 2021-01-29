// 功能 注册页面用户输入的数据满足需求，返回动态效果显示

var vm = new Vue({
    el:'#app',
    //替换页面上语法显示数据语法{{}}为[[]]，避免django框架模板语法冲突
    delimiters: ['[[',']]'],
    data: {
        error_name: false,//用户显示错误信息的判断字段
        error_name_message: '请输入5-20个字符用户名',
        username: '',//用户数据
        error_password: false,
        error_password_message: '请输入5-20个字符密码',
        password: '',
        error_check_password: false,
        error_password2_message: '密码不一致',
        password2:'',
        error_phone_message: '号码不正确',
        error_phone: false,
        phone: '',
        allow: true,
        error_allow: false,
        error_allow_message: '请勾选用户协议',
        host: '127.0.0.1:8000'
    },
    methods: {
        //检查用户名
        //@blur="check_username"
        check_username:function (){
            var re = /^[a-zA-Z0-9_-]{5,12}$/;
            if(re.test(this.username)){
                this.error_name = false;

            }else {
                this.error_name_message = '清输入5-12个字符用户名';
                this.error_name = true;
            }
            console.log('err')
            if(this.error_name == false){
                //axios.js发送http请求，访问一个链接 get请求
                //定义一个链接
                var url =  '/username/' + this.username + '/count/';
                //调试：查看数据
                console.log(url);
                /*axios语法：
                axios.get(服务器网址,{数据格式:指定服务器发送过来的数据}).then(response=>{
                    可以获取服务器发送过来的数据
                }).catch(error=>{
                    捕获异常/错误信息
                })
                */
                axios.get(url,{
                    responseType:'json'//json类似字典{数据名称:数据}
                }).then(response=>{
                    if (response.data.count>0){
                        //查询用户名个数
                        console.log(response.data.count)
                        this.error_name = true
                        this.error_name_message = '用户已存在'
                    }
                }).catch(error=>{
                    console.log(error)
                })
            }
        },
        //检查密码
        check_pwd:function (){
            var re = /^[a-zA-Z0-9_-]{5,12}$/;
            if(re.test(this.password)){
                this.error_password = false;
            }else {
                this.error_password = true;
            }
        },
        //确认密码 一致性
        check_cpwd: function (){
            if(this.password != this.password2){
                //不相同，设置为为真显示错误消息
                this.error_check_password = true;
            }else {
                this.error_check_password = false;
            }
        },
        //确认手机号满足规则
        check_phone: function (){
            var re = /^0[89]0\d{8}$$/;
            if(re.test(this.phone)){
                this.error_phone = false;
            }else {
                this.error_phone = true;
            }
        },
        //确认是否勾选协议
        check_allow: function (){
            if(this.allow){
                this.error_allow = false;
            }else {
                this.error_allow = true;
            }
        },
        //on_submit 提交表单，用户输入的数据满足所有规则才能提交
        //@submit="on_submit"用户提交事件
        on_submit(){
            this.check_allow();
            this.check_pwd();
            this.check_cpwd();
            this.check_username();
            this.check_phone();
            if(this.error_allow || this.error_name || this.error_password || this.error_check_password || this.error_phone){
                window.event.returnValue = false
            }
        }
    }
});
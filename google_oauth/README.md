# google 登录的一种不用安装依赖的流程

##### 流程

- 前端拼出来一个 auth url, 去小窗找 google 拿到 auth code

  - 前端发请求到后端， 把 username, …, email, auth_code 给到后端

  - 后端用 auth_code 去 google 换到 access_token, 用 access_token 拿到用户的 email

  - 注册完毕

- 简化内容

  - 后端不需要 callback 接口, 只需要一个 register 接口

  - 不需要安装 google 依赖（印象里几个依赖挺大的）

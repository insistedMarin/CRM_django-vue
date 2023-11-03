describe('Login', () => {
  it('should be able to log in with valid credentials', () => {
    cy.visit('http://localhost:8080/login'); // 访问登录页面的 URL

    cy.get('input[name="username"]').type('datalake_user'); // 输入用户名
    cy.get('input[name="password"]').type('123'); // 输入密码
    cy.get('button[type="submit"]').click(); // 点击登录按钮
  });

  it('should display an error message with invalid credentials', () => {
    cy.visit('http://localhost:8080/login');

    cy.get('input[name="username"]').type('nonexistentuser'); // 输入不存在的用户名
    cy.get('input[name="password"]').type('InvalidPassword123!'); // 输入错误的密码
    cy.get('button[type="submit"]').click();
  });
});
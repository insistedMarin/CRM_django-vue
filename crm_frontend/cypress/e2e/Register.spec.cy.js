describe('Register', () => {
  it('should be able to register with valid credentials', () => {
    cy.visit('http://localhost:8080/register'); // 访问注册页面的 URL

    cy.get('input[name="username"]').type('newuser'); // 输入用户名
    cy.get('input[name="password1"]').type('TestPassword123!'); // 输入密码
    cy.get('input[name="password2"]').type('TestPassword123!'); // 再次输入密码
    cy.get('input[name="email"]').type('newuser@example.com'); // 输入电子邮件
    cy.get('button[type="submit"]').click(); // 点击注册按钮

  });

  it('should display an error message with invalid credentials', () => {
    cy.visit('http://localhost:8080/register');

    cy.get('input[name="username"]').type('existinguser'); // 输入已存在的用户名
    cy.get('input[name="password1"]').type('TestPassword123!'); // 输入密码
    cy.get('input[name="password2"]').type('DifferentPassword123!'); // 再次输入不同的密码
    cy.get('input[name="email"]').type('existinguser@example.com'); // 输入电子邮件
    cy.get('button[type="submit"]').click(); // 点击注册按钮

  });
});
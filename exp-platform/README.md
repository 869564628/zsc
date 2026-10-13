# Experience Platform｜经验平台

这是一个静态网页小站，包含两个可独立使用的单文件应用：

- [平台首页](index.html)
- [深度经验库](deepexperience.html)：按学科分类整理学习路径、方法论、资源和避坑经验。
- [灵感经验站](vibeexperience.html)：记录轻量灵感、学习心得和即时想法。

## 部署到 GitHub Pages

本项目放在账号 `869564628` 的现有仓库 `zsc` 的 `exp-platform/` 目录中。仓库已加入 GitHub Actions 自动部署工作流：修改 `exp-platform/` 内的文件并推送到 `main` 后，会自动尝试发布网站。

**首次发布需要手动启用 Pages：**

1. 打开 [仓库 Settings](https://github.com/869564628/zsc/settings/pages)。
2. 在 **Build and deployment → Source** 中选择 **GitHub Actions**。
3. 打开 [Actions 工作流](https://github.com/869564628/zsc/actions/workflows/deploy-exp-platform.yml)，确认部署任务运行成功。

发布成功后的地址应为：

- https://869564628.github.io/zsc/
- https://869564628.github.io/zsc/deepexperience.html
- https://869564628.github.io/zsc/vibeexperience.html

若工作流报错，请打开 Actions 中最新一次运行，查看失败步骤。GitHub Pages 是否已经启用以及部署能否成功，需以仓库 Settings 和 Actions 的实际状态为准。

## GitHub 数据同步

网页默认把数据保存在当前浏览器的 `localStorage`。需要云端备份时，在网页内打开「设置 → GitHub 同步」：

- GitHub 用户名/组织：`869564628`
- 仓库名：`zsc`
- 数据文件名：`experience-data.json`
- 分支：`main`
- Token：向仓库推送数据通常需要具有该仓库内容写入权限的 Personal Access Token；公开仓库读取公开数据通常不需要 Token。

**安全提醒：** 不要把 Token 写进 HTML、提交到仓库或分享给他人。只在自己的浏览器设置中填写；公开仓库中的 `experience-data.json` 对任何人可见，请勿存放个人敏感信息。首次推送前请确认网页显示的仓库、分支和文件路径正确。

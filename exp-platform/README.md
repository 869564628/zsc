# Experience Platform｜经验平台

这是一个静态网页小站，包含两个可独立使用的单文件应用：

- [深度经验库](deepexperience.html)：按学科分类整理学习路径、方法论、资源和避坑经验。
- [灵感经验站](vibeexperience.html)：记录轻量灵感、学习心得和即时想法。
- [平台首页](index.html)：进入两个子站。

## 部署说明

本项目当前放在账号 `869564628` 的现有仓库 `zsc` 下的 `exp-platform/` 目录中。若仓库的 GitHub Pages 已启用，并将发布源设置为 `main` 分支的根目录，网页地址为：

- https://869564628.github.io/zsc/exp-platform/
- https://869564628.github.io/zsc/exp-platform/deepexperience.html
- https://869564628.github.io/zsc/exp-platform/vibeexperience.html

如果页面暂时无法访问，请进入仓库 **Settings → Pages**，将 **Build and deployment → Source** 设为 **Deploy from a branch**，Branch 选 **main**，目录选 **/(root)**，保存并等待部署完成。当前 GitHub 集成无法直接修改 Pages 设置，因此这一步需要在 GitHub 网页上确认。

## GitHub 数据同步

网页默认把数据保存在当前浏览器的 `localStorage`。需要云端备份时，在网页内打开「设置 → GitHub 同步」：

- GitHub 用户名/组织：`869564628`
- 仓库名：`zsc`
- 数据文件名：`experience-data.json`
- 分支：`main`
- Token：推送数据时通常需要具有该仓库内容写入权限的 Personal Access Token；公开数据的读取通常不需要 Token。

**安全提醒：** 不要把 Token 写进 HTML、提交到仓库或分享给他人。只在自己的浏览器设置中填写；公开仓库中的 `experience-data.json` 对任何人可见，请勿存放个人敏感信息。请在首次推送前确认网页显示的仓库、分支和文件路径正确。

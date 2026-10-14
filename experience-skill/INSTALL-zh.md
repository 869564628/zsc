# Experience Skill 安装与更新说明

## 安装到其他 AI

1. 解压 `experience-skill-v1.0.0.zip`。
2. 如果目标 AI 支持导入 Skill 文件夹或 ZIP，选择解压后的 `experience` 文件夹。
3. 如果它只允许上传单个文件，上传根目录中的 `SKILL.md`。这仍然能使用主要的经验整理规则，但不会自动附带网页文件和模板。
4. 用下面这句话测试：

   `把我这段经历整理成一条 Deep Experience，并标出哪些信息还需要核实。`

不同 AI 对 Skill 的格式和导入入口支持不同，所以这是一份可移植的 Skill 包，不是所有产品都通用的一键安装程序。

## 随时更新

Skill 的源文件维护在 GitHub：

https://github.com/869564628/zsc/tree/main/experience-skill

网页源文件维护在：

https://github.com/869564628/zsc/tree/main/exp-platform

如果已解压并安装 Python 3，可以在包目录运行：

```bash
python scripts/update_from_github.py
```

脚本会从 GitHub 下载最新 Skill 说明、模板和两个网页文件。更新完成后，检查版本和变更，再按目标 AI 的要求重新上传或安装。更新脚本不会替你登录 AI 产品，也不会自动把更新推送进已安装的 Skill。

已安装的 Skill 不会因为 GitHub 更新而自动变化，除非对应 AI 产品明确支持远程源和自动刷新。最稳妥的方式是将 GitHub 作为唯一源版本，每次更新后重新下载或运行脚本，再重新导入更新后的 Skill。

## Skill 与个人经验数据不是一回事

这个 Skill 规定 AI 应该如何记录、整理和检索经验；它不会自动读取浏览器里保存的个人经验。需要 AI 处理已有数据时，请先在网页中导出 JSON，再将文件提供给 AI。不要把 GitHub Token、密码、私密对话或保密研究数据提交到公开仓库。
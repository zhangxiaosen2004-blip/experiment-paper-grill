# 在网页版 ChatGPT 使用

本仓库提供纯 skill 插件，不带 MCP 服务、登录服务或后台程序。期刊调研使用当前 ChatGPT 会话可用的联网搜索能力。插件不会额外授予搜索、文件读取或其他工具权限。

## 先在自己的账号创建

以下方式适用于已开放插件创建功能、且可使用 Plugin Creator 的账号或工作区。

1. 在网页版 ChatGPT 的插件目录中安装 Plugin Creator。
2. 新建聊天，输入 `@`，选择 Plugin Creator。
3. 附加仓库中的 `skills/experiment-paper-grill/SKILL.md`。需要示例时，一并附加 `examples/journal-calibrated-review.md`。
4. 发送下面的创建要求，并按照 Plugin Creator 的实际提示完成创建和安装。

```text
请在我的账号中创建一个私人插件，名称为 Experiment Paper Grill。

把我附加的 SKILL.md 作为插件的核心技能，保留其科学评审流程。它应当先确认目标期刊，使用当前可用的联网搜索能力调查期刊，再按该期刊和交叉学科背景校准追问深度。

每轮只问一个问题，并提供简短的推荐回答方向。先检查已经提供的材料，避免要求我背诵可检索的事实。保留黑盒实验、公式理解和证据边界的检查。

创建纯 skill 插件，不添加 MCP 服务或外部账号连接。缺少搜索能力时明确说明限制，不虚构期刊政策。请完成私人插件创建，并告诉我如何在新聊天中选择它。
```

安装完成后，在新聊天的 `@` 菜单中选择 Experiment Paper Grill，再上传论文、公式或实验材料。确认它先询问目标期刊，且每轮只问一个问题。

如果搜不到 Plugin Creator，先核对账号、工作区权限和功能开放情况。当前仓库和 ZIP 包的存在，无法证明插件已在你的网页账号安装成功。

## 标准插件包

仓库根目录的 `plugin.json` 和 `skills/` 组成标准 Agent Plugins 包。生成提交用 ZIP：

```shell
python scripts/build_plugin.py
```

输出位于仓库同级的 `plugin-packages/experiment-paper-grill-plugin-1.0.0.zip`，其中 `plugin.json` 位于 ZIP 根目录。它用于插件打包与提交，向普通聊天附加 ZIP 不会自动安装插件。

如需面向所有人公开分发，可将此包提交到 OpenAI 插件发布平台。发布身份、权限、自动检查和审核结果，以平台实际要求为准。GitHub 公开仓库与 ChatGPT 插件目录是独立的发布渠道。

当前包已完成本地结构检查，尚未通过 OpenAI 发布平台检查，也未完成网页版账号安装和实际对话验证。

## 官方说明

- [网页版创建和使用插件](https://learn.chatgpt.com/docs/build-plugins)
- [标准插件包格式](https://developers.openai.com/plugins/build/plugins)
- [公开提交与发布](https://developers.openai.com/plugins/deploy/submission)

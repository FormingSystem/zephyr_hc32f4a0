---
id: learning.zephyr-docs.west.install
title: 安装 west
kind: engineering
status: maintained
domains: [zephyr, west]
source_url: https://docs.zephyrproject.org/latest/develop/west/install.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第1章\_安装west

原文：[Installing west](https://docs.zephyrproject.org/latest/develop/west/install.html)。读取日期：2026-10-12，`latest`。

west 用 Python 3 编写，通过 [PyPI](https://pypi.org/project/west/) 分发。可以使用 `pip3` 安装或升级。

## 1.1\_安装与检查

Linux 原文命令：

```bash
# Linux 终端；这是原文的用户级安装分支。
pip3 install --user -U west
```

Windows 和 macOS 原文命令：

```text
pip3 install -U west
```

关于 `--user` 的更多解释，见[Python 与 pip](../getting_started/P003_入门之后.md#python-and-pip)。安装之后，运行 `pip3 show -f west` 可以查看启动程序和相关文件的安装位置。west 安装好后，即可用它[克隆 Zephyr 仓库](../getting_started/P002_入门指南.md)。

> 译注：官方入门主线使用 Python 虚拟环境。已有环境应先检查并复用；虚拟环境内不要额外添加 `--user`。`-U` 表示升级已有软件包，执行前应考虑当前项目版本约束。

## 1.2\_程序结构

west 的代码以同名 Python 包 `west` 在 PyPI 分发。包内包含启动程序，也叫 `west`，Windows 上为 `west.exe`。

安装时，`pip3` 把启动程序放在文件系统的相应位置。具体目录取决于操作系统，但应该能由 `PATH` 找到。这个启动程序是命令行入口，既可执行 `west init`、`west update` 等内置命令，也可执行当前工作区发现的扩展命令。

除命令行外，还可直接调用 west 的 Python 接口，见 [West APIs](https://docs.zephyrproject.org/latest/develop/west/west-apis.html)。

## 1.3\_启用Shell补全

west 支持 Bash、Zsh、Fish 和 PowerShell 的命令补全。PowerShell 当前仅支持开发板限定符补全。

启用补全需要获取并加载相应脚本。以下为不同 shell 的独立分支，只选择实际使用的一种。

### 1.3.1\_Bash

临时启用，在能运行 west 的 Bash 中执行：

```bash
source <(west completion bash)
```

持久设置：

```bash
west completion bash > ~/west-completion.bash; printf '\n%s\n' "source ~/west-completion.bash" >> ~/.bashrc
```

该命令保存补全脚本，并在 Bash 启动文件中追加加载语句。

### 1.3.2\_Zsh

临时启用：

```zsh
source <(west completion zsh)
```

持久设置：

```zsh
west completion zsh > "${fpath[1]}/_west"
```

### 1.3.3\_Fish

临时启用：

```fish
west completion fish | source
```

持久设置：

```fish
west completion fish > $HOME/.config/fish/completions/west.fish
```

### 1.3.4\_PowerShell

临时启用：

```powershell
west completion powershell | Out-String | Invoke-Expression
```

原文的持久设置步骤为：

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
New-item -type file -force $PROFILE
west completion powershell > $HOME/west-completion.ps1
(Add-Content -Path $PROFILE -Value ". '{$HOME/west-completion.ps1}'")
```

> 译注：以上是原文脚本，不是本次执行记录。`$PROFILE` 指当前 PowerShell 配置文件；`New-Item -Force` 可能覆盖已有文件。已经存在的个人配置应先保留并直接追加所需加载语句，不应无条件重建。补全脚本是 west 生成的文件，不属于 Zephyr 源码原有文件。

---

<!-- reading-navigation:start -->

**主线阅读**

[本模块主线目录](../reading/west.md) · [全部主线](../reading/README.md) · [下一篇：west 基本概念](P002_基本概念.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[返回大纲](大纲.md) · [下一章：基本概念](P002_基本概念.md)

</details>

<!-- reading-navigation:end -->

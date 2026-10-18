---
id: learning.zephyr-docs.toolchains.gnu-arm
title: GNU Arm Embedded
kind: engineering
status: maintained
domains: [zephyr, toolchains]
source_url: https://docs.zephyrproject.org/latest/develop/toolchains/gnu_arm_embedded.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第4章\_GNU Arm Embedded

原文：[GNU Arm Embedded](https://docs.zephyrproject.org/latest/develop/toolchains/gnu_arm_embedded.html)。读取日期：2026-10-12，`latest`。

## 4.1\_下载并安装

从 [GNU Arm Embedded 下载页面](https://developer.arm.com/downloads/-/gnu-rm)取得适合主机操作系统的版本，安装并解压到文件系统中。

在 Windows 上，原文使用名为 `gnu_arm_embedded` 的目录作为安装示例。也可以使用 ARM GCC 安装器的默认位置，但必须相应调整后续环境变量。

macOS Catalina 或更新版本上，可能需要[调整安全策略](../getting_started/P008_macOS补充配置.md)，工具链才能从终端运行。

> 译注：安装位置由读者选择，不绑定盘符。下列路径输出以 `<工具链安装目录>` 代替原文的机器路径；占位符不是要输入的命令。选用 **软件开发工具包（Software Development Kit，SDK）** 工具链时不需要再额外安装本工具链。

## 4.2\_设置并检查环境变量

按[环境变量](P003_环境变量.md)的方式设置：

- `ZEPHYR_TOOLCHAIN_VARIANT` 为 `gnuarmemb`。
- `GNUARMEMB_TOOLCHAIN_PATH` 为工具链安装目录。

检查当前环境是否正确，可以对照以下会话。实际安装目录可能不同；`$` 和 `>` 是提示符，后续行是示例输出。

```text
# Linux、macOS：
$ echo $ZEPHYR_TOOLCHAIN_VARIANT
gnuarmemb
$ echo $GNUARMEMB_TOOLCHAIN_PATH
<工具链安装目录>

# Windows cmd.exe：
> echo %ZEPHYR_TOOLCHAIN_VARIANT%
gnuarmemb
> echo %GNUARMEMB_TOOLCHAIN_PATH%
<工具链安装目录>
```

## 4.3\_macOS的补充方法

原文警告：如果前述方法遇到问题，可尝试 Homebrew 中的非官方包。运行：

```bash
# macOS 终端；已安装 Homebrew。
brew install gcc-arm-embedded
```

随后仍设置 `ZEPHYR_TOOLCHAIN_VARIANT=gnuarmemb`，并将 `GNUARMEMB_TOOLCHAIN_PATH` 设为 Homebrew 安装目录，例如 `/usr/local`。

> 译注：这是上游页面列出的备选方法，并非本次重新测试的 Homebrew 配方或默认路径。应以实际包状态、主机架构及安装结果确定路径，不能因示例用了 `/usr/local` 就忽略其他布局。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：环境变量](P003_环境变量.md) · [本模块主线目录](../reading/toolchains.md) · [全部主线](../reading/README.md) · [下一篇：其他交叉编译器](P005_其他交叉编译器.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：环境变量](P003_环境变量.md) · [返回大纲](大纲.md) · [下一章：其他交叉编译器](P005_其他交叉编译器.md)

</details>

<!-- reading-navigation:end -->

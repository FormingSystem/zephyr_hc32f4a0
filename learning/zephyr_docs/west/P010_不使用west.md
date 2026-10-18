---
id: learning.zephyr-docs.west.west_without
title: 不使用west
kind: reference
status: maintained
domains: [zephyr, documentation]
source_url: https://docs.zephyrproject.org/latest/develop/west/without-west.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第10章\_不使用west

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/west/without-west.html)。本次读取日期：2026-10-14；基线为所保存的 `latest` 页面，HTML摘要见[来源记录](../SOURCES.md)。

本页说明如何在不使用 west 的情况下使用 Zephyr。由于需要额外工作，官方不建议初学者采用此路线，尤其需要手工替代以下功能：

- 除主 `zephyr` 仓库外，克隆 Zephyr 使用的其他源码仓库，并持续更新。
- 向 Zephyr 构建系统指定这些仓库的位置。
- 原本无需理解底层主机工具详细用法就能完成的烧录与调试。

**原文注意：**若以前安装过 west，现在决定停止使用，先卸载它：

```shell
pip3 uninstall west
```

否则 Zephyr 构建系统仍会发现 west，并可能尝试使用它。

> 译注：这是选择“完全不使用 west”路线时的原文步骤，不是阅读本章的前置操作。卸载影响当前命令对应的 Python 环境，本次翻译没有执行它。

## 10.1\_取得源码

除下载 Zephyr 源码仓库本身，还必须手动克隆该仓库中 **west清单（West Manifest）**列出的附加项目，并检出清单指定的修订：

```shell
mkdir zephyrproject
cd zephyrproject
git clone https://github.com/zephyrproject-rtos/zephyr
# clone additional repositories listed in zephyr/west.yml,
# and check out the specified revisions as well.
```

更新 `zephyr` 仓库时，也需要维护这些附加仓库：按需要加入新增项目，并将已有项目更新到相应修订。

> 译注：代码注释要求同时克隆并检出 `zephyr/west.yml` 指定的版本。“更新”应与所用清单一致，不是独立追踪每个模块任意分支的最新提交。`zephyrproject` 是示例工作区名。

## 10.2\_构建应用

只要手动指定所需模块，即使没有安装 west，也可直接用 CMake 和 Ninja（或 make）构建 Zephyr 应用：

```shell
cmake -Bbuild -GNinja -DZEPHYR_MODULES=module1;module2;... samples/hello_world
ninja -Cbuild
```

> 译注：原文将分号列表直接写在命令行中；在 Bash 等将分号视为命令分隔符的终端，应将完整参数写成 `'-DZEPHYR_MODULES=module1;module2;...'`。`module1` 等必须替换为实际模块路径，`...` 不是有效模块。原例也未指定开发板，实际构建须从配置或追加的 `-DBOARD=...` 取得目标；源码相对路径按 Zephyr 源码根解析。上方保留原代码以供对照。

安装了 west 时，Zephyr 构建系统会使用它设置 `ZEPHYR_MODULES`。未安装 west 且应用不需要任何附加仓库时，构建仍然可用；如果应用需要其中的仓库，就必须像上面那样自己设置 `ZEPHYR_MODULES`。详见[模块与外部项目](../modules/P001_模块与外部项目.md)。

同样，若应用需要**二进制块（Binary Blob）**而又不使用 west，就必须自行下载，并放在正确位置，替代 `west blobs` 的工作。详见[官方二进制块说明](../contributing/P008_二进制文件.md#bin-blobs)。

## 10.3\_烧录与调试

[构建、烧录与调试](P007_构建烧录与调试.md)中介绍的 `west flash`、`west debug`、`west debugserver`、`west attach` 和 `west rtt` 都依赖 west；不使用 west 时，这些命令不可用。

仍可直接调用适合目标开发板的[烧录与调试主机工具](../debugging/P004_烧录与调试主机工具.md)，它们也是上述 west 命令包装的工具；此时必须自行提供适用于开发板和应用的正确参数。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：二进制镜像签名](P009_二进制镜像签名.md) · [本模块主线目录](../reading/west.md) · [全部主线](../reading/README.md) · [下一篇：内置命令](P011_内置命令.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：二进制镜像签名](P009_二进制镜像签名.md) · [返回大纲](大纲.md) · [下一章：内置命令](P011_内置命令.md)

</details>

<!-- reading-navigation:end -->

---
id: learning.zephyr-docs.languages.lang-rust
title: Rust语言支持
kind: reference
status: maintained
domains: [zephyr, languages]
source_url: https://docs.zephyrproject.org/latest/develop/languages/rust/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第8章\_Rust语言支持

原文：[Rust Language Support](https://docs.zephyrproject.org/latest/develop/languages/rust/index.html)。读取日期：2026-10-12，`latest`。

**Rust（现代系统编程语言）**旨在兼顾内存安全、并发能力、性能与底层控制。其**所有权模型（Ownership Model）**通过编译期检查，帮助避免空指针解引用和数据竞争等常见错误。

Rust 对安全性与正确性的重视，使它适用于嵌入式等对可靠性要求较高的环境。它提供较强的抽象能力，不要求传统的运行时系统或**垃圾回收器（Garbage Collector）**，可同时表达高层逻辑与底层硬件交互。这些特征适合 Zephyr 所面向的资源受限、重视系统稳定性的项目。

> 译注：原文是在概括语言设计。Rust 的安全保证依赖相应语言边界；`unsafe`、跨语言接口和外设操作仍需要正确实现。它不会自动验证硬件接线、外设时序或整个应用行为。

## 8.1\_启用Rust支持

下面按官方顺序说明模块、应用配置与构建入口。所有操作都面向已经存在的 Zephyr 工作区，不要求重新初始化工作区。

### 8.1.1\_取得可选语言模块

Rust 当前是可选模块，最简启用方式是通过 west：

```sh
west config manifest.project-filter +zephyr-lang-rust
west update
```

完成后，Rust 支持应位于工作区的 `modules/lang/rust`。

> 译注：`manifest.project-filter` 是 west 的项目过滤配置，`+zephyr-lang-rust` 表示纳入该清单项目；`west update` 才下载或更新模块。它会按当前清单处理项目，不只是创建一个同名目录。这里没有执行这两个命令，也没有改动现有实验工作区。

### 8.1.2\_应用配置

在应用 `prj.conf` 中启用 Kconfig 选项 `CONFIG_RUST`。最方便的起点是 `modules/lang/rust/samples` 中的[官方示例](https://github.com/zephyrproject-rtos/zephyr-lang-rust/blob/dd73abc242e995784da62352fe8c70d9a6c7ac2e/samples)，因为它也包含下一步所需 CMake 设置。

### 8.1.3\_CMake入口

应用的 `CMakeLists.txt` 需要接入 Rust 构建。可参考示例，基本结构如下。包查找参数 `REQUIRED` 表示缺包时报错，`HINTS` 提供搜索提示；`$ENV{ZEPHYR_BASE}` 用 `ENV` 语法读取 Zephyr 源码根环境变量：

```cmake
cmake_minimum_required(VERSION 3.28.0)

find_package(Zephyr REQUIRED HINTS $ENV{ZEPHYR_BASE})

project(my_app)
rust_cargo_application()
```

> 译注：CMake 函数 `rust_cargo_application()` 由 Rust 支持模块提供，用于把 **Cargo（Rust包管理与构建工具）**接入 Zephyr 应用。`ZEPHYR_BASE` 是源码根环境变量；仅在文件中写下函数名而没有正确取得、发现模块，不会自动安装支持。

### 8.1.4\_Cargo清单

创建应用的 `Cargo.toml` 描述 Rust 构建。原文 Hello World 示例为；其中 Apache-2.0 与 MIT 是许可证名称，原例的 `license` 字段列出这两种许可：

```toml
[package]
# This must be rustapp for now.
name = "rustapp"
version = "0.1.0"
edition = "2021"
description = "The description of my app"
license = "Apache-2.0 or MIT"

[lib]
crate-type = ["staticlib"]

[dependencies]
zephyr = "0.1.0"
log = "0.4.22"
```

唯一必需的依赖是 `zephyr`，它提供与 Zephyr 交互的 **crate（Rust编译单元与代码包组织单位）**。原例还列出 `log`，用于示例日志支持。

> 译注：按这份原例，包名暂时必须为 `rustapp`，`crate-type = ["staticlib"]` 生成静态库供整体固件链接，`edition = "2021"` 选择语言版次。版本号和包名约束属于原文所示模块接口，不能据此推断任意未来模块版本均相同；许可证字段也应按自己项目实际许可填写。

### 8.1.5\_构建目标限制

此后像普通 Zephyr 应用一样构建。原文指出当前只有少数目标支持 Rust，列表位于模块的 [etc/platforms.txt](https://github.com/zephyrproject-rtos/zephyr-lang-rust/blob/dd73abc242e995784da62352fe8c70d9a6c7ac2e/etc/platforms.txt)。

> 译注：上面两个模块源码链接保留官方文档给出的固定提交号；实际工作区通过 west 取得哪个修订，应以当前清单为准。

## 8.2\_API文档

模块最新版本的 **应用程序编程接口（Application Programming Interface，API）**文档发布在 [官方GitHub Pages](https://zephyrproject-rtos.github.io/zephyr-lang-rust/nostd/zephyr/index.html)。在线文档面向通用目标，并启用全部特性。

已有可构建应用后，可以为自己的目标生成文档：

```text
west build -t rustdoc

...

Generated <构建目录>/doc/rust/target/riscv32i-unknown-none-elf/doc/rustapp/index.html
```

> 译注：`west build -t rustdoc` 在已配置的应用构建环境执行，`...` 与 `Generated` 行是示意输出，不是需要输入的命令。原文输出中带机器目录的路径已替换为 `<构建目录>` 占位；应打开本次工具实际打印的路径，不能照抄示例中的目标三元组或目录位置。

最后输出的页面可以用浏览器打开。顶层是应用自己的文档；左侧找到 `zephyr` crate 后可进入 Zephyr 接口文档。同次生成也会包括应用直接或间接使用的依赖文档。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：C加加语言支持](P007_C加加语言支持.md) · [本模块主线目录](../reading/languages.md) · [全部主线](../reading/README.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：C++语言支持](P007_C加加语言支持.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->

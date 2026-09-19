---
id: learning-cmake-2
title: 接入 Zephyr 模块
kind: tutorial
status: ready
domains: [embedded, tools]
---
<!-- SPDX-License-Identifier: Apache-2.0 -->

# 2. 接入 Zephyr 模块

## 2.1 三种“模块”先分开

[上一章](P01_把源文件和库加入构建.md)的 scale 是普通 CMake 库。Zephyr module 是带元数据的源码目录，告诉 Zephyr 到哪里读 CMake、Kconfig 等入口。west project 则是清单里的 Git 仓库。这三者可以组合，但名称相近不等于同一件事：west 下载了代码，不代表应用就会编译代码。

本章使用仓库里的 [zephyr_module](labs/zephyr_module/zephyr/module.yml) 和 [zephyr_app](labs/zephyr_app/CMakeLists.txt)，不联网获取新模块。先按[项目环境](../../project-docs/environment.md)建立 .venv 和 SDK；当前位置仍是仓库根目录。

## 2.2 一个最小模块有哪些入口

```text
zephyr_module/
  zephyr/module.yml
  CMakeLists.txt
  Kconfig
  include/scale.h
  src/scale.c
```

module.yml 声明模块名 learning_scale，并指定相对于模块根目录的 CMake 目录与 Kconfig 文件。Kconfig 定义布尔选项 LEARNING_SCALE；应用配置写 CONFIG_LEARNING_SCALE=y。

模块 CMake 在该符号开启时调用 zephyr_library、zephyr_library_sources，并公开 include 路径。关闭后源码不应参与编译。应用 main 也用同一条件决定是否调用函数，避免模块关闭后留下未定义引用。

## 2.3 在应用发现 Zephyr 之前追加模块

实验应用明确使用当前仓库的 Zephyr 与两个基础模块，然后在 find_package 之前追加模块。
CMSIS（Common Microcontroller Software Interface Standard）提供 Arm 微控制器通用支持；HAL（Hardware Abstraction Layer，硬件抽象层）在这里是华大芯片支持代码。它们的来源由项目锁定记录确定。
ZEPHYR_BASE 是 Zephyr 源码根目录变量；find_package 的 REQUIRED 关键字表示找不到就终止，HINTS 提供搜索位置提示。
target_sources 的 PRIVATE 仍表示源码仅属于 app 目标，含义与上一章相同：

```cmake
list(APPEND EXTRA_ZEPHYR_MODULES
     "${CMAKE_CURRENT_LIST_DIR}/../zephyr_module")
find_package(Zephyr REQUIRED HINTS "${ZEPHYR_BASE}")
project(learning_module)
target_sources(app PRIVATE src/main.c)
```

CMAKE_CURRENT_LIST_DIR 指当前 CMake 文件目录，与终端从哪里运行无关。EXTRA_ZEPHYR_MODULES 让工程在已有基础模块外增加本应用模块。当前 project_env.py 已设置基础 ZEPHYR_MODULES；不要只改同名普通 CMake 变量然后假定它覆盖环境输入。

模块发现发生在 find_package 期间，放在之后就太晚。查生成的 zephyr_modules.txt、Kconfig.modules 和 compile_commands.json，可分别验证“发现了目录”“读到了选项”“实际编译了源文件”。三种证据不应混为一谈。[官方模块说明](https://docs.zephyrproject.org/latest/develop/modules.html)

## 2.4 开启与关闭分别运行一次

```bash
source .venv/Scripts/activate
python scripts/project_env.py exec python scripts/twister -p mps2/an386 -T learning/cmake/labs/zephyr_app --short-build-path --outdir build/learning-tools/module-test --inline-logs
```

Twister 是 Zephyr 的测试编排工具，本章先借它运行两个现成场景；[板级 P03](../board/P03_用Twister和QEMU验证配置.md)解释参数与报告。tests.yaml 中 enabled 使用 prj.conf，disabled 叠加 no_module.conf。预期 2/2 执行通过，分别匹配 module result=42 和 module disabled。

Windows 下 --short-build-path 通过短构建路径避免工具对长对象文件路径的限制；报告仍在指定 outdir。切勿把构建出错归因于业务源码之前，跳过错误日志里的文件路径。

在 module-test 内搜索生成的 .config 与 compile_commands.json：开启场景的 .config 是 y，编译命令包含 zephyr_module/src/scale.c；关闭场景应为未设置且没有该源文件的编译命令。若只看模块目录存在，无法证明条件编译生效。

## 2.5 常见失败与修改实验

找不到 LEARNING_SCALE：模块未发现或 Kconfig 入口路径错，先看 CMake 配置日志，不能在生成的 .config 手改补救。scale.h 不可见：确认模块开启及 include 声明。链接找不到 scale_sample：确认模块源文件入库且调用者与模块开关一致。

练习把 scale_sample 的倍数改为 3：先预测启用场景输出 63、关闭场景不变，再修改 enabled 场景预期字符串，运行两个场景。也可新增第二个源文件，并在模块 zephyr_library_sources 中登记，比较编译数据库。

工程常用习惯是保持模块公共接口小、私有源码封装、开关关闭仍可构建；增加平台依赖时显式写 Kconfig 依赖及测试平台约束。引入外部模块先核对版本与许可证，不能只贴本机路径。

## 2.6 如何把实验迁移到项目

本项目长期源码可以树内维护，并在实际应用 find_package 前追加该目录。若要成为受控基础依赖，需要同步 dependencies.lock.json、模块选择和源码审计规则；不能让项目入口悄悄引用相邻源码树。

本实验产物仅在 build/learning-tools/module-test。保留源码与清单，产物可在不运行测试时清理；Windows junction 只作为构建辅助，不手动沿链接递归删除源码目录。

完成标志是两个场景都运行通过，且能从配置和编译命令解释差异。[CMake 大纲](大纲.md) · [VS Code 调试](../vscode/P01_搭建编译与单步调试环境.md)

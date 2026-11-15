---
id: learning.zephyr-docs.board-samples.page-88
title: 蓝牙Mesh徽章
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/phytec/reel_board/mesh_badge/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="mesh_badge"></a>

# 第88章\_蓝牙 Mesh 徽章（Bluetooth Mesh badge）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/phytec/reel_board/mesh_badge/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/phytec/reel_board/mesh_badge/README.rst/..)

<a id="overview"></a>

## 88.1 概述（Overview）

本 reel board 应用演示蓝牙 Mesh 功能。

应用起初作为普通蓝牙 GATT 外设运行。可在手机上安装 Android 或 iOS 版 nRF Connect，访问应用公开的服务；也可以使用电脑上的任意蓝牙低功耗 GATT 客户端访问，不过以下说明着重介绍手机操作。

> 译注——术语：GATT 是通用属性配置文件（Generic Attribute Profile），Mesh 是网状网络。这里先通过普通蓝牙连接写入徽章文字，再转入 Mesh；它不是手机在每次问候时都保持 GATT 连接的方案。

<a id="steps-to-set-up"></a>

## 88.2 设置步骤（Steps to set up）

1. 在手机的 nRF Connect 中扫描设备，查找“reel board”。

2. 连接设备，可看到一个服务，选择它。

3. 点击向上箭头图标，请求向特征（Characteristic）写入。

4. 选择“Text”（文本），以文本而非十六进制方式输入。

5. 输入姓名或其他任意文本，允许多个由空格分隔的词。reel 显示屏所用字体可显示三行文本，每行最多十二个字符；可用逗号强制换行。

> 译注——显示限制：原文三行、每行十二字符描述的是所用字体布局，不保证任意 Unicode 字符都有字形。写入长度由 CONFIG_BT_DEVICE_NAME_MAX 限制且按字节检查；汉字等多字节 UTF-8 内容不能简单按十二个字估算缓冲区。

6. 点击“Send”（发送）；由于这是受保护的特征，会触发配对（Pairing）。配对口令（Passkey）显示在板上，请在手机中输入该口令。

7. 配对完成后，开发板显示发送的文本；若不满意，可继续写入其他内容。

8. 确认文本后，断开与开发板的连接，可退出应用或返回设备扫描页。

9. 断开连接后，开发板切换到蓝牙 Mesh 模式，此后不能再通过 GATT 连接它。

> 译注——切换条件：本次 disconnected() 只有在设备名已不同于 CONFIG_BT_DEVICE_NAME 且 Mesh 尚未初始化时才启动 Mesh。仅连接后立即断开，或写回完全相同的默认名称，并不满足这个条件。

按同样方式配置多块板后，它们可以通过 Mesh 通信。按开发板用户按钮，会把已存文本的第一个词，即姓名，发送给网络中其他板，使它们显示“<name> says hi!”，也就是“某某向你问好”。

> 译注——问候内容：发送函数取遇到空格、逗号或换行前的第一段，再限制为 HELLO_MAX=8 字节；并非任意长度的首词都会完整发送。示例自配网使用固定演示网络密钥和应用密钥，这解释了同配置徽章能直接通信，不应把它当作生产部署的独立安全配网流程。

要把开发板恢复到初始状态，即禁用 Mesh、擦除已存文本，并重新允许 GATT 连接：

> 译注——重置范围：启动时检测到按钮按住后，board_init() 调用 erase_storage() 擦除整个存储分区，而不只是改掉屏幕上的姓名；原有设置也会丢失。本次没有执行该复位或擦除操作。

1. 按住用户按钮再上电；如果已经供电，则按住用户按钮并按复位按钮。

2. 等待屏幕显示“Resetting Device”（正在重置设备）。

<a id="see-also"></a>

## 88.3 另请参阅（See also）

[单色字符帧缓冲（Monochrome Character Framebuffer）](../hardware/P184_单色字符帧缓冲接口.md)

[蓝牙 Mesh（Bluetooth Mesh）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html)

[通用属性配置文件（Generic Attribute Profile，GATT）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html)

[蓝牙 API（Bluetooth APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bluetooth.html)

> 译注——源码入口：[src/main.c](../../../samples/boards/phytec/reel_board/mesh_badge/src/main.c)；[src/mesh.c](../../../samples/boards/phytec/reel_board/mesh_badge/src/mesh.c)；[src/reel_board.c](../../../samples/boards/phytec/reel_board/mesh_badge/src/reel_board.c)。仓库参照使用相对路径，版本可能与本次上游快照不同。

对应官方文档源码：[samples/boards/phytec/reel_board/mesh_badge/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/phytec/reel_board/mesh_badge/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/phytec/reel_board/mesh_badge/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P087_Microchip示例目录.md) · [返回大纲](大纲.md) · [下一章](P089_reel_board示例目录.md)

---
id: zephyr-p006-lab-files
title: P006 普通组件与应用源码原件
kind: reference
status: evolving
---

# P006 源码原件

本目录保存正文逐个讲解的9个完整文件：components/app_greeting提供模块声明、配置开关和问候函数；applications/component_hello提供应用入口、main及开启/关闭配置。它们是本章编写的普通组件，不包含厂商HAL或HC32板适配。

按 [P013正文](../../P013_自定义源码模块与配置开关.md#section-13-1) 在G:/zephyr_practice下创建同样结构。可使用 [创建组件](../../commands/P006_Windows/create-greeting-component.txt) 和 [创建应用](../../commands/P006_Windows/create-component-application.txt)，两块都会在目标已存在时停止，不覆盖已有修改。原件在文档仓库中存在，不表示已进入G盘构建。

配套 9 个文件曾与实验副本逐字节核对，启用/关闭构建和 QEMU 输出的历史验证范围见 [P013 13.1.12](../../P013_自定义源码模块与配置开关.md#section-13-1-12)。复现时仍需核对自己使用的源码、工具与生成结果。

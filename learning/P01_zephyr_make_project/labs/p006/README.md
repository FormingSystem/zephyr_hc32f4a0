---
id: zephyr-p006-lab-files
title: P006 普通组件与应用源码原件
kind: reference
status: evolving
---

# P006 源码原件

本目录保存正文逐个讲解的9个完整文件：components/app_greeting提供模块声明、配置开关和问候函数；applications/component_hello提供应用入口、main及开启/关闭配置。它们是本章编写的普通组件，不包含厂商HAL或HC32板适配。

按 [P006正文](../../P006_HC32与外部源码模块接入_Windows.md#section-6-7) 在G:/zephyr_practice下创建同样结构。可使用 [创建组件](../../commands/P006_Windows/create-greeting-component.txt) 和 [创建应用](../../commands/P006_Windows/create-component-application.txt)，两块都会在目标已存在时停止，不覆盖已有修改。原件在文档仓库中存在，不表示已进入G盘构建。

本轮9文件与G盘创建结果逐字节一致。启用/关闭构建和QEMU输出均完成验证；具体范围见正文6.7.12。

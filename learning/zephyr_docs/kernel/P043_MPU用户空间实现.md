---
id: learning.zephyr-docs.kernel.mpu-userspace
title: MPU用户空间实现
kind: reference
status: maintained
domains: [zephyr, kernel, userspace, mpu]
source_url: https://docs.zephyrproject.org/latest/kernel/usermode/mpu_userspace.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第43章\_MPU用户空间实现

原文：[MPU Backed Userspace](https://docs.zephyrproject.org/latest/kernel/usermode/mpu_userspace.html)。读取日期：2026-10-12，`latest`。

基于 **内存保护单元（Memory Protection Unit，MPU）** 的用户空间需要一组辅助栈，与系统定义的线程栈一一对应。原文描述这些特权栈在构建时创建。

后处理脚本 `scripts/build/gen_kobject_list.py` 扫描生成的 **可执行与可链接格式（Executable and Linkable Format，ELF）** 文件，查找线程栈对象，创建特权栈、查找表及辅助函数并加入镜像。相关构建步骤见[CMake构建系统](../build_system/P001_CMake构建系统.md)。

线程降到用户模式时填入特权栈信息，之后上下文切换和系统调用设施据此配置线程栈及可选保护区的 MPU 区域。

系统调用期间会验证用户线程调用权限及参数，并在特权栈上执行指定内核接口；返回后恢复用户模式与用户栈。

> 译注：原页叙述把“参数验证”写在“提权”之前，但验证函数本身运行在内核侧。实际流程先通过受控陷阱进入特权入口，再验证并调用实现，见[系统调用](P044_系统调用.md)。特权栈的生成和动态分配细节也应以目标架构与版本为准，不能仅凭本短页推断所有架构只有同一构建方案。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：MPU栈对象](P042_MPU栈对象.md) · [本模块主线目录](../reading/kernel.md) · [全部主线](../reading/README.md) · [下一篇：系统调用](P044_系统调用.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：MPU栈对象](P042_MPU栈对象.md) · [下一章：系统调用](P044_系统调用.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->

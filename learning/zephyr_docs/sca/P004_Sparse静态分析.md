---
id: learning.zephyr-docs.sca.sca-sparse
title: Sparse静态分析
kind: reference
status: maintained
domains: [zephyr, sca]
source_url: https://docs.zephyrproject.org/latest/develop/sca/sparse.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第4章\_Sparse静态分析

原文：[Sparse support](https://docs.zephyrproject.org/latest/develop/sca/sparse.html)。读取日期：2026-10-12，`latest`。

[Sparse](https://www.kernel.org/doc/html/latest/dev-tools/sparse.html) 是静态代码分析工具。除一般分析外，它支持 `address_space` 属性，用于在 C 代码中区分不同的**地址空间（Address Space）**，检查指向不同空间的指针是否被混用。

## 4.1\_带缓存地址与不带缓存地址

Sparse 还支持 `force` 属性，用于不同地址空间指针之间的显式转换。原文说明 Zephyr 当前定义了一个自有地址空间 `__cache`，标识 Xtensa 架构中来自带缓存地址范围的指针，帮助发现**缓存地址（Cached Address）**与**非缓存地址（Uncached Address）**混用的情况。

> 译注：这里的地址空间是静态检查使用的类型区分，不是声明硬件只有一个地址空间，也不是说带缓存与非缓存指针可任意互换。`__cache` 是 Zephyr 的源码标注名称，不能由名称推断其可用于其他架构。

## 4.2\_运行Sparse验证构建

在 `west build` 后传入 `-DZEPHYR_SCA_VARIANT=sparse`：

```sh
west build -d hello -b intel_adsp/cavs25 zephyr/samples/hello_world -- -DZEPHYR_SCA_VARIANT=sparse
```

> 译注：原例在包含 `zephyr/` 子目录的 west 工作区根，用 Bash 执行；`-d hello` 指定生成的构建目录。它选择 `intel_adsp/cavs25` 目标，需要对应工具链、依赖及可找到的 Sparse 工具。若当前已在 Zephyr 源码根，应将示例路径改为 `samples/hello_world`。本次没有执行验证构建。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Clang静态分析](P003_Clang静态分析.md) · [本模块主线目录](../reading/sca.md) · [全部主线](../reading/README.md) · [下一篇：头文件依赖检查](P005_头文件依赖检查.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：Clang静态分析](P003_Clang静态分析.md) · [返回大纲](大纲.md) · [下一章：头文件依赖检查](P005_头文件依赖检查.md)

</details>

<!-- reading-navigation:end -->

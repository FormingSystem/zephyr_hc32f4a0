---
id: learning.zephyr-docs.storage.zmsapi-1
title: Zephyr内存存储数据结构目录
kind: reference
status: maintained
domains: [zephyr, storage]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__zms__data__structures.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第58章\_Zephyr内存存储数据结构目录

原文：[group__zms__data__structures](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__data__structures.html)。读取日期：2026-10-13，`latest`。

## 58.1\_结构与类型

**Zephyr 内存存储（Zephyr Memory Storage，ZMS）**的结构、类型与宏来自 `zephyr/kvss/zms.h`。

- [`struct zms_fs`](https://docs.zephyrproject.org/latest/doxygen/html/structzms__fs.html)：文件系统实例。
- [`struct zms_iter_config`](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter__config.html)：供 [`zms_iter_init_with_config()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga2c839e3cceb3fd4931a2ffc26726ca34) 使用的**迭代器配置（Iterator Configuration）**。
- [`struct zms_iter`](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter.html)：供 [`zms_iter_next()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#gaba4e19c06a27a5287e9f8507a4fa11c3) 和 [`zms_iter_next_all()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#gaa37ba625bd4835acf772b0cdb38a3348) 使用的**不透明迭代器状态（Opaque Iterator State）**。

[`zms_id_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__data__structures.html#ga0509b3dce3030a56ecff866d693944f9) 是接口使用的标识符类型；[`zms_iter_predicate_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__data__structures.html#ga73c4c209bc4fbb8125781088b15eef64) 是带配置初始化时使用的**谓词回调（Predicate Callback）**类型，以标识符作为参数，返回布尔值。

```c
typedef uint32_t zms_id_t;
typedef bool (*zms_iter_predicate_t)(zms_id_t id);
```

原页面显示上述 [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) 声明，同时明确指出：标识符类型的实际宽度取决于 Kconfig 配置项 [`CONFIG_ZMS_ID_64BIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZMS_ID_64BIT)。

## 58.2\_内嵌数据大小

**分配表条目（Allocation Table Entry，ATE）**可以直接保存小块数据。[`ZMS_DATA_IN_ATE_SIZE`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__data__structures.html#ga758c42a254d0e64596c35c7ac644aedc) 宏定义可直接存入 ATE 的最大数据字节数：

```c
#define ZMS_DATA_IN_ATE_SIZE 8
```

长度不超过此值的数据保留在 ATE 内，而不放入扇区数据区。此容量取决于 [`CONFIG_ZMS_ID_64BIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZMS_ID_64BIT)；上面保留的是当前参考页显示的值。它也是 [`zms_iter_next()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#gaba4e19c06a27a5287e9f8507a4fa11c3) / [`zms_iter_next_all()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#gaa37ba625bd4835acf772b0cdb38a3348) 能复制到调用者缓冲区的最大数据量。

## 58.3\_迭代过滤默认值

**范围过滤（Range Filtering）**决定可接受的最小、最大标识符；**掩码过滤（Mask Filtering）**通过位掩码筛选标识符。下列宏分别定义默认下界、上界及接受全部标识符的掩码：

```c
#define ZMS_ITER_ID_MIN ((zms_id_t)0)
#define ZMS_ITER_ID_MAX ((zms_id_t)~(zms_id_t)0)
#define ZMS_ITER_MASK_ALL ZMS_ITER_ID_MAX
```

[`ZMS_ITER_CONFIG_DEFAULT`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__data__structures.html#ga1ee4de45e9df1784664fcba45e9a8788) 是 `struct zms_iter_config` 的默认初始化器（Default Initializer），原始展开如下：

```c
{ \
        .mask_id = ZMS_ITER_MASK_ALL, \
        .min_id = ZMS_ITER_ID_MIN, \
        .max_id = ZMS_ITER_ID_MAX, \
        .use_mask = false, \
        .use_range = false, \
        .use_predicate = false, \
        .predicate_func = NULL, \
}
```

## 58.4\_挂载选项

枚举 `enum zms_mount_flags` 定义 [`zms_mount()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga962625b12f21cf030a35c944a2de380e) 与 [`zms_mount_force()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#gab5a3adcdc5eecbb8a1bcb9d1c7709837) 的**挂载（Mount）**选项。`BIT(0)` 是第 0 位的位掩码。

```c
enum zms_mount_flags {
    ZMS_MOUNT_FLAG_NO_FORMAT = BIT(0)
};
```

[`ZMS_MOUNT_FLAG_NO_FORMAT`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__data__structures.html#gga5f9a7529c95876c29b6a0fd7a230fc92a0b00eefe2f9cc169d285ad8255521c87) 表示挂载时不要格式化已擦除介质（Erased Media）。当设置此标志，且底层闪存区域已擦除、没有有效 ZMS 头部时，挂载失败，而不是创建新头部。

---

[上一章：Zephyr内存存储参考目录](P057_Zephyr内存存储参考目录.md) · [下一章：Zephyr内存存储接口](P059_Zephyr内存存储接口.md) · [返回大纲](大纲.md)

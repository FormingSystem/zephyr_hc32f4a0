---
id: learning.zephyr-docs.cmake-reference.module.yaml
title: yaml
kind: reference
status: maintained
domains: [zephyr, cmake]
source_url: https://docs.zephyrproject.org/latest/build/cmake-ref/module/yaml.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_yaml

原文：[yaml](https://docs.zephyrproject.org/latest/build/cmake-ref/module/yaml.html)。本次读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

<a id="module:yaml"></a>

本模块为 Zephyr 构建系统提供 YAML 文件的读取、写入和操作功能，支持基本键值对（Key-value Pair）、嵌套对象（Nested Object）、列表（List）以及映射列表（List of Maps）。

## 18.1\_支持的YAML功能（Supported YAML Features）

基本键值对：

```yaml
foo: bar
```

嵌套对象：

```yaml
foo:
  bar: baz
```

简单列表：

```yaml
foos:
  - foo1
  - foo2
  - foo3
```

映射列表：

```yaml
foo:
  - bar: val1
    baz: val1
  - bar: val2
    baz: val2
```

## 18.2\_使用示例（Example Usage）

加载模块，创建 YAML 上下文（Context），设置一个值和一个列表，向列表追加一个映射，然后保存到文件。代码末尾的注释展示 `my_file.yaml` 的预期内容。

```cmake
include(yaml)

# Create a new YAML context
yaml_create(NAME my_yaml FILE my_file.yaml)

# Set some values
yaml_set(NAME my_yaml KEY foo VALUE bar)
yaml_set(NAME my_yaml KEY list LIST item1 item2 item3)

# Append a map to a list
yaml_set(NAME my_yaml KEY list APPEND LIST MAP "name: test, value: 42")

# Save the context to file
yaml_save(NAME my_yaml)

# my_file.yaml now contains:
#
# foo: bar
# list:
#   - item1
#   - item2
#   - item3
#   - name: test
#     value: 42
```

## 18.3\_命令（Commands）

<a id="command:yaml_context"></a>

### 18.3.1\_yaml_context

查询 YAML 上下文的状态。

```cmake
yaml_context(EXISTS NAME <name> <result>)
```

- `EXISTS`：检查 YAML 上下文是否存在于当前作用域（Scope）。若存在，在 `<result>` 中返回 `TRUE`。
- `NAME <name>`：YAML 上下文名称。
- `<result>`：保存查询结果的变量。

<a id="command:yaml_create"></a>

### 18.3.2\_yaml_create

创建新的空 YAML 上下文。

```cmake
yaml_create(NAME <name> [FILE <file>])
```

- `NAME <name>`：YAML 上下文名称。
- `FILE <file>`：与此上下文配合使用的文件路径；调用 `yaml_save()` 时使用这个文件。

<a id="command:yaml_load"></a>

### 18.3.3\_yaml_load

把已有 YAML 文件加载到 YAML 上下文。

```cmake
yaml_load(FILE <file> NAME <name>)
```

- `FILE <file>`：要加载的文件路径。
- `NAME <name>`：YAML 上下文名称。

<a id="command:yaml_get"></a>

### 18.3.4\_yaml_get

从 YAML 上下文获取某个键的值。

```cmake
yaml_get(<out-var> NAME <name> KEY <key>...)
```

- `NAME <name>`：YAML 上下文名称。
- `KEY <key>...`：要获取的键名；可指定多个键，实现嵌套访问。
- `<out-var>`：保存所获取值的变量。

若键表示一个列表，返回该列表。如果键指向复杂对象（Complex Object），行为未定义（Undefined Behavior）。

<a id="command:yaml_length"></a>

### 18.3.5\_yaml_length

获取某个键所定义数组（Array）的长度。

```cmake
yaml_length(<out-var> NAME <name> KEY <key>...)
```

- `NAME <name>`：YAML 上下文名称。
- `KEY <key>...`：定义列表的键名。
- `<out-var>`：保存长度的变量。

如果该键未定义数组，返回 `-1`。

<a id="command:yaml_set"></a>

### 18.3.6\_yaml_set

在 YAML 上下文中设置一个值或值列表。

```cmake
yaml_set(NAME <name> KEY <key>... [GENEX] VALUE <value>)
yaml_set(NAME <name> KEY <key>... [APPEND] [GENEX] LIST <value>...)
yaml_set(NAME <name> KEY <key>... [APPEND] LIST MAP <map1> MAP <map2> MAP ...)
```

- `NAME <name>`：YAML 上下文名称。
- `KEY <key>...`：要设置的键名。
- `VALUE <value>`：键的新值。
- `LIST <values>`：键的新值列表。
- `APPEND`：将值列表追加到已有列表。
- `GENEX`：这些值包含生成器表达式（Generator Expression）。
- `MAP <map>`：含键值对的映射；各对之间用 `,` 分隔，键和值之间用 `:` 分隔。格式为 `"<key1>: <value1>, <key2>: <value2>, ..."`。向列表添加映射时，可使用多个 `MAP` 参数区分各个映射。不能与 `GENEX` 一起使用。

**注意：**如果映射的值包含逗号，必须用单引号括起该值，并对逗号进行双重转义（Double Escape）：`'A \\,string'`。

<a id="command:yaml_remove"></a>

### 18.3.7\_yaml_remove

从 YAML 上下文移除一个键。

```cmake
yaml_remove(NAME <name> KEY <key>...)
```

- `NAME <name>`：YAML 上下文名称。
- `KEY <key>...`：要移除的键名；可指定多个键，实现嵌套访问。

<a id="command:yaml_save"></a>

### 18.3.8\_yaml_save

将 YAML 上下文写入文件。

```cmake
yaml_save(NAME <name> [FILE <file>])
```

- `NAME <name>`：YAML 上下文名称。
- `FILE <file>`：写入上下文的文件路径；未给出时，使用上下文的 `FILE` 属性。

如果上下文使用了生成器表达式，包含它们的键最初会以注释形式写入。完整内容在构建时才可用。依赖文件内容完整的构建步骤，必须依赖 `name_yaml_saved` 目标。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：git](P017_git.md) · [本模块主线目录](../reading/cmake_reference.md) · [全部主线](../reading/README.md) · [下一篇：LIBC_LINK_LIBRARIES](P019_LIBC_LINK_LIBRARIES.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P017_git.md) · [返回大纲](大纲.md) · [下一章](P019_LIBC_LINK_LIBRARIES.md)

</details>

<!-- reading-navigation:end -->

---
id: learning.zephyr-docs.hardware.ztestapi-0
title: FFF测试扩展接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__fff__extensions.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第500章\_FFF测试扩展接口

原文：[group__fff__extensions](https://docs.zephyrproject.org/latest/doxygen/html/group__fff__extensions.html)。读取日期：2026-10-13，`latest`。

本模块扩展**伪函数框架（Fake Function Framework，FFF）**，简化伪函数的配置与使用。接口位于 `zephyr/fff_extensions.h`，用于为自定义伪函数提供每次调用专用的上下文数据。

## 500.1\_包装自定义处理逻辑

[`RETURN_HANDLED_CONTEXT`](https://docs.zephyrproject.org/latest/doxygen/html/group__fff__extensions.html#ga4a4e81f6291e0bfbe7f60e0a03c2e9b1) 宏包装自定义伪函数的函数体，从中提取用户定义的**上下文结构（Context Structure）**。使用者无需熟悉 FFF 的内部实现即可按后面的例子编写伪函数。

```c
#define RETURN_HANDLED_CONTEXT(FUNCNAME, CONTEXTTYPE, RESULTFIELD, CONTEXTPTRNAME, HANDLERBODY)
```

| 参数 | 官方说明译文 |
| --- | --- |
| `FUNCNAME` | 被伪装函数的名称 |
| `CONTEXTTYPE` | 用户自定义的伪函数上下文结构类型 |
| `RESULTFIELD` | 保存返回类型及返回值的字段名称 |
| `CONTEXTPTRNAME` | 指向用户上下文结构的指针所使用的名称 |
| `HANDLERBODY` | 内嵌的自定义伪函数处理逻辑 |

下面保留官方展开。`return_val_seq`、`return_val_seq_len` 和 `return_val_seq_idx` 是 FFF 控制结构中的返回值序列、长度和当前位置；`return_val` 为默认返回值。`CONTAINER_OF` 是从成员指针取得所属结构指针的辅助宏，`contexts` 与 `seq_idx` 是展开内部的上下文数组指针和序列索引。`##` 是 C 预处理器的标记拼接运算符。

```c
if (FUNCNAME##_fake.return_val_seq_len) {                                                  \
        CONTEXTTYPE * const contexts =                                                     \
                CONTAINER_OF(FUNCNAME##_fake.return_val_seq, CONTEXTTYPE, RESULTFIELD);    \
        size_t const seq_idx =                                                             \
                (FUNCNAME##_fake.return_val_seq_idx < FUNCNAME##_fake.return_val_seq_len)  \
                        ? FUNCNAME##_fake.return_val_seq_idx++                             \
                        : FUNCNAME##_fake.return_val_seq_idx - 1;                          \
        CONTEXTTYPE * const CONTEXTPTRNAME = &contexts[seq_idx];                           \
        HANDLERBODY;                                                                       \
}                                                                                          \
return FUNCNAME##_fake.return_val
```

## 500.2\_按调用上下文返回结果

官方示例定义一个包含实例指针和结果值的上下文结构，再在处理函数中读取该上下文。结果为 `0` 且输出指针非空时，示例将实例指针写到 `instance_out`；最后返回相应的结果值。

其中 `struct instance` 是示例使用的实例类型，`FUNCNAME##_custom_fake_context` 是上下文类型名称模板，`result` 是结果字段，`context` 为上下文指针，`NULL` 为 C 空指针值。

```c
struct FUNCNAME##_custom_fake_context
{
    struct instance * const instance;
    int result;
};

int FUNCNAME##_custom_fake(
    const struct instance **instance_out)
{
    RETURN_HANDLED_CONTEXT(
        FUNCNAME,
        struct FUNCNAME##_custom_fake_context,
        result,
        context,
        {
            if (context != NULL)
            {
                if (context->result == 0)
                {
                    if (instance_out != NULL)
                    {
                        *instance_out = context->instance;
                    }
                }
                return context->result;
            }
            return FUNCNAME##_fake.return_val;
        }
    );
}
```

> 译注：示例保留了官方 `FUNCNAME##...` 占位写法。`##` 用于宏替换列表，不能把这些占位拼接直接当作普通 C 函数名编译；实际使用时应结合具体被替代函数的名称及 FFF 配置。

---

[上一章：测试API目录](P499_测试API目录.md) · [下一章：ZTest基准测试接口](P501_ZTest基准测试接口.md) · [返回大纲](大纲.md)

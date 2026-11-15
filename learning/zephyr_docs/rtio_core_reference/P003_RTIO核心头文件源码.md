---
id: learning.zephyr-docs.rtio-core-reference.page-3
title: RTIO核心头文件源码
kind: reference
status: maintained
domains: [zephyr, hardware, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rtio_2rtio_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_RTIO核心头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/rtio_2rtio_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；完整接口说明见[头文件参考](P002_RTIO核心头文件参考.md)和[公共API](P001_RTIO公共接口.md)。

## 3.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00083"></a>
<a id="foldopen00161"></a>
<a id="foldopen00175"></a>
<a id="foldopen00334"></a>
<a id="foldopen00349"></a>
<a id="foldopen00362"></a>
<a id="foldopen00390"></a>
<a id="foldopen00428"></a>
<a id="foldopen00443"></a>
<a id="foldopen00475"></a>
<a id="foldopen00496"></a>
<a id="foldopen00512"></a>
<a id="foldopen00546"></a>
<a id="foldopen00570"></a>
<a id="foldopen00584"></a>
<a id="foldopen00630"></a>
<a id="foldopen00722"></a>
<a id="foldopen00735"></a>
<a id="foldopen00751"></a>
<a id="foldopen00808"></a>
<a id="foldopen00885"></a>
<a id="foldopen00912"></a>
<a id="foldopen01011"></a>
<a id="foldopen01132"></a>
<a id="foldopen01217"></a>
<a id="aapp__memdomain_8h_html"></a>
<a id="aatomic_8h_html"></a>
<a id="acqe_8h_html"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="agroup__atomic__apis_html_ga1c1693d524c49d11fd32b323a39d718e"></a>
<a id="agroup__atomic__apis_html_ga33bb426a17535bd1022895a7e44b32fa"></a>
<a id="agroup__atomic__apis_html_ga7ff45e13aa5f8be5d7a550e49f5c720b"></a>
<a id="agroup__atomic__apis_html_gaae47a9cbe5a6534967b417f602b37ac2"></a>
<a id="agroup__atomic__apis_html_gab879da5aa1ffcc317adc664c016586f7"></a>
<a id="agroup__clock__apis_html_ga0bb4b83f0222193b21a8910311bab0ca"></a>
<a id="agroup__clock__apis_html_ga3d9541cfe2e8395af66d186efa77362f"></a>
<a id="agroup__clock__apis_html_ga509cf4599c1f162c97540743e8c21d33"></a>
<a id="agroup__clock__apis_html_ga87d0d7a0f7bcdcc8c4909962eac12985"></a>
<a id="agroup__clock__apis_html_ga9abf00b34e16ab7ad0883603b6778b1b"></a>
<a id="agroup__isr__apis_html_ga8482b0dd2283d12677a9ebe321667d16"></a>
<a id="agroup__mem__blocks__apis_html_ga39e7f8dfe3bda8eabc2372f9a1e87342"></a>
<a id="agroup__mem__blocks__apis_html_ga72614d0c120f40209837b77d0333bb23"></a>
<a id="agroup__mpsc__lockfree_html_ga403add133841ef88e10d74141e782b37"></a>
<a id="agroup__mpsc__lockfree_html_ga823ec37b84ac43e46167aac954bce9d7"></a>
<a id="agroup__rtio__cqe__flags_html_ga087465f866d417d5332602bb582cc1a7"></a>
<a id="agroup__rtio__cqe__flags_html_ga0b5f3f7e7be472ecf87bd2b08c1888da"></a>
<a id="agroup__rtio__cqe__flags_html_ga0f212500447a5e37e225a6997953b609"></a>
<a id="agroup__rtio__cqe__flags_html_ga28b3a5661248b6b3763aab47417114d6"></a>
<a id="agroup__rtio__cqe__flags_html_gaef64ea020a20ac22a0edcb6eca032efc"></a>
<a id="agroup__rtio__ops_html_gafeb05c351207cd1638fa78f6607e1a4a"></a>
<a id="agroup__rtio__sqe__flags_html_ga2802b46584220afffa0e959e149d5a4d"></a>
<a id="agroup__rtio__sqe__flags_html_ga7f7f9b038ab8409f271b1aebc1b95ee6"></a>
<a id="agroup__rtio_html_ga05e24d59485f71cc0126d44abbe8cf2b"></a>
<a id="agroup__rtio_html_ga1f4fb7bccbaae08a94387e4b11275a78"></a>
<a id="agroup__rtio_html_ga37c94f84cfce3810fd598040aba3841e"></a>
<a id="agroup__rtio_html_ga4213be028b0a1264daaa0d30c4c2d089"></a>
<a id="agroup__rtio_html_ga4abc221d5a90ab882000a72caa0ebd0f"></a>
<a id="agroup__rtio_html_ga6530bf56ccbab046a362a6448f941609"></a>
<a id="agroup__rtio_html_ga65e351af0a16dcf504a51ef4eb9316c7"></a>
<a id="agroup__rtio_html_ga6adaa4d7ef1fa8054000d8d9b8e634bd"></a>
<a id="agroup__rtio_html_ga6f55202adeca60aed0343a7a0dcab071"></a>
<a id="agroup__rtio_html_ga75661c8c6c94a0ac6254cec674b478c8"></a>
<a id="agroup__rtio_html_ga830863e6c8d9b96f4c473a038cab8f8c"></a>
<a id="agroup__rtio_html_ga86a38086dd85150ab6e479d73db1c6d1"></a>
<a id="agroup__rtio_html_ga8b47c954d15a334621def53acceb6799"></a>
<a id="agroup__rtio_html_ga9486fb7b50e8d2409a50da235203536b"></a>
<a id="agroup__rtio_html_ga98b2bbef95aea342a9b86a9775dd5c3b"></a>
<a id="agroup__rtio_html_ga98b8f272b175ff2c0e9f5ed420c3abcc"></a>
<a id="agroup__rtio_html_ga9ab6490aa1893ae01bb0938a34c3e248"></a>
<a id="agroup__rtio_html_ga9da42c98546930575525f0f92710f9e4"></a>
<a id="agroup__rtio_html_gaa0799a5f8ad98425d385a07c5d27d9cb"></a>
<a id="agroup__rtio_html_gaab6843e2038d00a8354f57d7e2ffcf7e"></a>
<a id="agroup__rtio_html_gaabf5e6876e04f92f99a860591c7d310a"></a>
<a id="agroup__rtio_html_gaada07aa6acefa548743b525225fa482f"></a>
<a id="agroup__rtio_html_gac01252e55d2848b38c0ed77b71d600a7"></a>
<a id="agroup__rtio_html_gacb1d2ffa2b07418d8a8aa319bd4336ab"></a>
<a id="agroup__rtio_html_gad848646651fdf3649b882e5268f72a3c"></a>
<a id="agroup__rtio_html_gae562cf241911804cdb9f4e3a73b53df4"></a>
<a id="agroup__rtio_html_gae63ffc626a3e99406d36aa47f10b49e1"></a>
<a id="agroup__rtio_html_gae690e3dc0fc40dda57257b2eed432719"></a>
<a id="agroup__rtio_html_gaedbf9386a36ed99baa290ef6c318ded1"></a>
<a id="agroup__rtio_html_gaf617d05d9b59ce1f1d0697617ef6f249"></a>
<a id="agroup__rtio_html_gafb6e8c8679cb9483445c510cd6f14741"></a>
<a id="agroup__rtio_html_gafee27c64a4a4989c4eb774addde8eb2e"></a>
<a id="agroup__semaphore__apis_html_ga1bd12d8d8c1b9c6be9b665d0fefe5562"></a>
<a id="agroup__semaphore__apis_html_gab9be3cf1988af2cd6afdace52d497c84"></a>
<a id="agroup__semaphore__apis_html_gac71e2383c1920dddc45a561cacfef090"></a>
<a id="agroup__subsys__tracing__macros_html_ga445bcac4cec53d560ddca757de17e1e3"></a>
<a id="agroup__subsys__tracing__macros_html_gab0350eef3ed26733e57505ee2d0487cb"></a>
<a id="agroup__subsys__tracing__macros_html_gadce691eea44f211b804ce44b51b2e71d"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="agroup__sys-util_html_gac5bc561d1bfd1bf68877fe577779bd2f"></a>
<a id="agroup__sys-util_html_gae664e7492e37d324831caf2321ddda37"></a>
<a id="agroup__system__errno_html_ga2d1678d5a7cc8ce499643f3b8957def4"></a>
<a id="agroup__system__errno_html_ga6a05c923dad0c1208043e9c20a58c8e5"></a>
<a id="agroup__system__errno_html_ga91457bbf35f0f1085619a99423bb1f33"></a>
<a id="agroup__thread__apis_html_ga08a3484c33444ecedc2d71d78495a295"></a>
<a id="agroup__thread__apis_html_ga7ef1ed0fb9513df8096ede1e52fc76b2"></a>
<a id="agroup__usermode__apis_html_ga94087bedf96fe2a2bea437d3d585ca22"></a>
<a id="agroup__usermode__apis_html_gab70fe65497da1347cc4b7bf7ca2daf22"></a>
<a id="aiodev_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="amem__blocks_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="asqe_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a3ea490c9b3617d4479bd80ef93cd5602"></a>
<a id="astdint_8h_html_a4788399d1d0b37ccf098a7da82254808"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astring_8h_html"></a>
<a id="astring_8h_html_a4137694174d4ca2fad886a1db355015c"></a>
<a id="astructk__mem__partition_html"></a>
<a id="astructk__sem_html"></a>
<a id="astructk__thread_html"></a>
<a id="astructk__timeout__t_html"></a>
<a id="astructk__timepoint__t_html"></a>
<a id="astructmpsc__node_html"></a>
<a id="astructmpsc_html"></a>
<a id="astructrtio__cqe_html"></a>
<a id="astructrtio__cqe_html_a15128387ccbea55812ef229eab7241e7"></a>
<a id="astructrtio__cqe_html_a8a7632ef1cfd31529d782bd761908d93"></a>
<a id="astructrtio__cqe_html_acbe2e6607a752b676d9336b9ca6ce435"></a>
<a id="astructrtio__iodev__sqe_html"></a>
<a id="astructrtio__iodev__sqe_html_a2bd98599678909c0ddb22f879affa12b"></a>
<a id="astructrtio__iodev__sqe_html_a3c3a050793589258eab5ff5ac30f24c8"></a>
<a id="astructrtio__iodev__sqe_html_a9cfdd004b65a5e2bc111bc2fb333498c"></a>
<a id="astructrtio__pool_html"></a>
<a id="astructrtio__pool_html_a5a148773dcd269e1d29be95c77fb6d99"></a>
<a id="astructrtio__pool_html_a89240a8b8e9809d3f61ef903d24e3db2"></a>
<a id="astructrtio__pool_html_abe49ac5f1cec586855dc5318e3091419"></a>
<a id="astructrtio__sqe_html"></a>
<a id="astructrtio__sqe_html_a0ed519ee0b5867ff73bdaf37f983c971"></a>
<a id="astructrtio__sqe_html_a1d8d3e3426e47a2c7f54d98f51acd953"></a>
<a id="astructrtio__sqe_html_a29e0c1b06b6f7b604af147a231b46319"></a>
<a id="astructrtio__sqe_html_a64f5db04d58882832f86477628c25be3"></a>
<a id="astructrtio__sqe_html_a67376f40a13960b152a23da250275722"></a>
<a id="astructrtio__sqe_html_aad2ff8524df0e24b812e77e2393bf5b0"></a>
<a id="astructrtio__sqe_html_ab71176c084e8b8eb65dfeb3018ae2a49"></a>
<a id="astructrtio__sqe_html_af8c31c33e9fedebe55cac73595d0f696"></a>
<a id="astructrtio_html"></a>
<a id="astructrtio_html_a1bce3c3bb0150275ece65975adf3ee4f"></a>
<a id="astructrtio_html_a34fbabfdbef3144f4520bf678684cdfb"></a>
<a id="astructrtio_html_a358de1033ab4396d1f1baee2699c993f"></a>
<a id="astructrtio_html_a955f012bac623e7c037b5f1dba8e7fda"></a>
<a id="astructrtio_html_ac45facdcc6d64cd70113b9b05b2fb086"></a>
<a id="astructrtio_html_ad6f44a354a170cb04a584beee7728fa9"></a>
<a id="asys_2iterable__sections_8h_html"></a>
<a id="asys_2util_8h_html"></a>
<a id="asyscall_8h_html_abc92c4d00c42f08c7600602c8847f021"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * SPDX-FileCopyrightText: Copyright (c) 2022 Intel Corporation
<a id="l00003"></a> * SPDX-FileCopyrightText: Copyright (c) 2026 Infineon Technologies AG,
<a id="l00004"></a> * SPDX-FileCopyrightText: or an affiliate of Infineon Technologies AG. All rights reserved.
<a id="l00005"></a> *
<a id="l00006"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00007"></a> */
<a id="l00008"></a>
<a id="l00028"></a>
<a id="l00029"></a>#ifndef ZEPHYR_INCLUDE_RTIO_RTIO_H_
<a id="l00030"></a>#define ZEPHYR_INCLUDE_RTIO_RTIO_H_
<a id="l00031"></a>
<a id="l00032"></a>#include &lt;string.h&gt;
<a id="l00033"></a>
<a id="l00034"></a>#include &lt;zephyr/app_memory/app_memdomain.h&gt;
<a id="l00035"></a>#include &lt;zephyr/device.h&gt;
<a id="l00036"></a>#include &lt;zephyr/kernel.h&gt;
<a id="l00037"></a>#include &lt;zephyr/sys/__assert.h&gt;
<a id="l00038"></a>#include &lt;zephyr/sys/atomic.h&gt;
<a id="l00039"></a>#include &lt;zephyr/sys/mem_blocks.h&gt;
<a id="l00040"></a>#include &lt;zephyr/sys/util.h&gt;
<a id="l00041"></a>#include &lt;zephyr/sys/iterable_sections.h&gt;
<a id="l00042"></a>#include &lt;zephyr/rtio/sqe.h&gt;
<a id="l00043"></a>#include &lt;zephyr/rtio/cqe.h&gt;
<a id="l00044"></a>#include &lt;zephyr/rtio/iodev.h&gt;
<a id="l00045"></a>
<a id="l00046"></a>#ifdef __cplusplus
<a id="l00047"></a>extern "C" {
<a id="l00048"></a>#endif
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00059"></a>
<a id="l00060"></a>struct rtio;
<a id="l00061"></a>
<a id="l00070"></a>typedef void (*rtio_cqe_callback_t)(struct rtio *r, void *user_data);
<a id="l00071"></a>
<a id="l00083"></a>struct rtio {
<a id="l00084"></a>#ifdef CONFIG_RTIO_SUBMIT_SEM
<a id="l00085"></a>        /* A wait semaphore which may suspend the calling thread
<a id="l00086"></a>         * to wait for some number of completions when calling submit
<a id="l00087"></a>         */
<a id="l00088"></a>        struct k_sem *submit_sem;
<a id="l00089"></a>
<a id="l00090"></a>        uint32_t submit_count;
<a id="l00091"></a>#endif
<a id="l00092"></a>
<a id="l00093"></a>#ifdef CONFIG_RTIO_CONSUME_SEM
<a id="l00094"></a>        /* A wait semaphore which may suspend the calling thread
<a id="l00095"></a>         * to wait for some number of completions while consuming
<a id="l00096"></a>         * them from the completion queue
<a id="l00097"></a>         */
<a id="l00098"></a>        struct k_sem *consume_sem;
<a id="l00099"></a>#endif
<a id="l00100"></a>
<a id="l00102"></a>        atomic_t cq_count;
<a id="l00103"></a>
<a id="l00105"></a>        atomic_t xcqcnt;
<a id="l00106"></a>
<a id="l00108"></a>        struct rtio_sqe_pool *sqe_pool;
<a id="l00109"></a>
<a id="l00111"></a>        struct rtio_cqe_pool *cqe_pool;
<a id="l00112"></a>
<a id="l00113"></a>#ifdef CONFIG_RTIO_SYS_MEM_BLOCKS
<a id="l00114"></a>        /* Mem block pool */
<a id="l00115"></a>        struct sys_mem_blocks *block_pool;
<a id="l00116"></a>#endif
<a id="l00117"></a>
<a id="l00119"></a>        struct mpsc sq;
<a id="l00120"></a>
<a id="l00122"></a>        struct mpsc cq;
<a id="l00123"></a>
<a id="l00124"></a>#ifdef CONFIG_RTIO_CQE_CALLBACK
<a id="l00125"></a>        /* Completion queue event callback */
<a id="l00126"></a>        rtio_cqe_callback_t cqe_cb;
<a id="l00127"></a>
<a id="l00128"></a>        /* Completion queue event callback user data */
<a id="l00129"></a>        void *cqe_cb_user_data;
<a id="l00130"></a>#endif
<a id="l00131"></a>};
<a id="l00132"></a>
<a id="l00133"></a>/* @cond ignore */
<a id="l00134"></a>#define Z_RTIO_DEFINE(name, _sqe_pool, _cqe_pool, _block_pool)                                     \
<a id="l00135"></a>        IF_ENABLED(CONFIG_RTIO_SUBMIT_SEM,                                                         \
<a id="l00136"></a>                   (static K_SEM_DEFINE(CONCAT(_submit_sem_, name), 0, K_SEM_MAX_LIMIT)))          \
<a id="l00137"></a>        IF_ENABLED(CONFIG_RTIO_CONSUME_SEM,                                                        \
<a id="l00138"></a>                   (static K_SEM_DEFINE(CONCAT(_consume_sem_, name), 0, K_SEM_MAX_LIMIT)))         \
<a id="l00139"></a>        STRUCT_SECTION_ITERABLE(rtio, name) = {                                                    \
<a id="l00140"></a>                IF_ENABLED(CONFIG_RTIO_SUBMIT_SEM, (.submit_sem = &amp;CONCAT(_submit_sem_, name),))   \
<a id="l00141"></a>                IF_ENABLED(CONFIG_RTIO_SUBMIT_SEM, (.submit_count = 0,))                           \
<a id="l00142"></a>                IF_ENABLED(CONFIG_RTIO_CONSUME_SEM, (.consume_sem = &amp;CONCAT(_consume_sem_, name),))\
<a id="l00143"></a>                .cq_count = ATOMIC_INIT(0),                                                        \
<a id="l00144"></a>                .xcqcnt = ATOMIC_INIT(0),                                                          \
<a id="l00145"></a>                .sqe_pool = _sqe_pool,                                                             \
<a id="l00146"></a>                .cqe_pool = _cqe_pool,                                                             \
<a id="l00147"></a>                IF_ENABLED(CONFIG_RTIO_SYS_MEM_BLOCKS, (.block_pool = _block_pool,))               \
<a id="l00148"></a>                .sq = MPSC_INIT((name.sq)),                                                        \
<a id="l00149"></a>                .cq = MPSC_INIT((name.cq)),                                                        \
<a id="l00150"></a>                IF_ENABLED(CONFIG_RTIO_CQE_CALLBACK, (.cqe_cb = NULL, .cqe_cb_user_data = NULL,))  \
<a id="l00151"></a>        }
<a id="l00152"></a>/* @endcond */
<a id="l00153"></a>
<a id="l00161"></a>#define RTIO_DEFINE(name, sq_sz, cq_sz)                                         \
<a id="l00162"></a>        Z_RTIO_SQE_POOL_DEFINE(CONCAT(name, _sqe_pool), sq_sz);                 \
<a id="l00163"></a>        Z_RTIO_CQE_POOL_DEFINE(CONCAT(name, _cqe_pool), cq_sz);                 \
<a id="l00164"></a>        Z_RTIO_DEFINE(name, &amp;CONCAT(name, _sqe_pool),                           \
<a id="l00165"></a>                      &amp;CONCAT(name, _cqe_pool), NULL)
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00175"></a>static inline size_t rtio_mempool_block_size(const struct rtio *r)
<a id="l00176"></a>{
<a id="l00177"></a>#ifndef CONFIG_RTIO_SYS_MEM_BLOCKS
<a id="l00178"></a>        ARG_UNUSED(r);
<a id="l00179"></a>        return 0;
<a id="l00180"></a>#else
<a id="l00181"></a>        if (r == NULL || r-&gt;block_pool == NULL) {
<a id="l00182"></a>                return 0;
<a id="l00183"></a>        }
<a id="l00184"></a>        return BIT(r-&gt;block_pool-&gt;info.blk_sz_shift);
<a id="l00185"></a>#endif
<a id="l00186"></a>}
<a id="l00187"></a>
<a id="l00195"></a>#if defined(CONFIG_RTIO_SYS_MEM_BLOCKS) || defined(__DOXYGEN__)
<a id="l00196"></a>static inline uint16_t __rtio_compute_mempool_block_index(const struct rtio *r, const void *ptr)
<a id="l00197"></a>{
<a id="l00198"></a>        uintptr_t addr = (uintptr_t)ptr;
<a id="l00199"></a>        struct sys_mem_blocks *mem_pool = r-&gt;block_pool;
<a id="l00200"></a>        uint32_t block_size = rtio_mempool_block_size(r);
<a id="l00201"></a>
<a id="l00202"></a>        uintptr_t buff = (uintptr_t)mem_pool-&gt;buffer;
<a id="l00203"></a>        uint32_t buff_size = mem_pool-&gt;info.num_blocks * block_size;
<a id="l00204"></a>
<a id="l00205"></a>        if (addr &lt; buff || addr &gt;= buff + buff_size) {
<a id="l00206"></a>                return UINT16_MAX;
<a id="l00207"></a>        }
<a id="l00208"></a>        return (addr - buff) / block_size;
<a id="l00209"></a>}
<a id="l00210"></a>#endif
<a id="l00211"></a>
<a id="l00213"></a>
<a id="l00214"></a>static inline int rtio_block_pool_alloc(struct rtio *r, size_t min_sz,
<a id="l00215"></a>                                          size_t max_sz, uint8_t **buf, uint32_t *buf_len)
<a id="l00216"></a>{
<a id="l00217"></a>#ifndef CONFIG_RTIO_SYS_MEM_BLOCKS
<a id="l00218"></a>        ARG_UNUSED(r);
<a id="l00219"></a>        ARG_UNUSED(min_sz);
<a id="l00220"></a>        ARG_UNUSED(max_sz);
<a id="l00221"></a>        ARG_UNUSED(buf);
<a id="l00222"></a>        ARG_UNUSED(buf_len);
<a id="l00223"></a>        return -ENOTSUP;
<a id="l00224"></a>#else
<a id="l00225"></a>        const uint32_t block_size = rtio_mempool_block_size(r);
<a id="l00226"></a>        uint32_t bytes = max_sz;
<a id="l00227"></a>
<a id="l00228"></a>        /* Not every context has a block pool and the block size may return 0 in
<a id="l00229"></a>         * that case
<a id="l00230"></a>         */
<a id="l00231"></a>        if (block_size == 0) {
<a id="l00232"></a>                return -ENOMEM;
<a id="l00233"></a>        }
<a id="l00234"></a>
<a id="l00235"></a>        do {
<a id="l00236"></a>                size_t num_blks = DIV_ROUND_UP(bytes, block_size);
<a id="l00237"></a>                int rc = sys_mem_blocks_alloc_contiguous(r-&gt;block_pool, num_blks, (void **)buf);
<a id="l00238"></a>
<a id="l00239"></a>                if (rc == 0) {
<a id="l00240"></a>                        *buf_len = num_blks * block_size;
<a id="l00241"></a>                        return 0;
<a id="l00242"></a>                }
<a id="l00243"></a>
<a id="l00244"></a>                if (bytes &lt;= block_size) {
<a id="l00245"></a>                        break;
<a id="l00246"></a>                }
<a id="l00247"></a>
<a id="l00248"></a>                bytes -= block_size;
<a id="l00249"></a>        } while (bytes &gt;= min_sz);
<a id="l00250"></a>
<a id="l00251"></a>        return -ENOMEM;
<a id="l00252"></a>#endif
<a id="l00253"></a>}
<a id="l00254"></a>
<a id="l00255"></a>static inline void rtio_block_pool_free(struct rtio *r, void *buf, uint32_t buf_len)
<a id="l00256"></a>{
<a id="l00257"></a>#ifndef CONFIG_RTIO_SYS_MEM_BLOCKS
<a id="l00258"></a>        ARG_UNUSED(r);
<a id="l00259"></a>        ARG_UNUSED(buf);
<a id="l00260"></a>        ARG_UNUSED(buf_len);
<a id="l00261"></a>#else
<a id="l00262"></a>        size_t num_blks = buf_len &gt;&gt; r-&gt;block_pool-&gt;info.blk_sz_shift;
<a id="l00263"></a>
<a id="l00264"></a>        sys_mem_blocks_free_contiguous(r-&gt;block_pool, buf, num_blks);
<a id="l00265"></a>#endif
<a id="l00266"></a>}
<a id="l00267"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00272"></a>extern struct k_mem_partition rtio_partition;
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>/* Do not try and reformat the macros */
<a id="l00276"></a>
<a id="l00286"></a>#if CONFIG_RTIO_BLOCK_POOL_PLACEMENT_DTCM
<a id="l00287"></a>#define RTIO_BMEM Z_GENERIC_SECTION(".dtcm_bss") static
<a id="l00288"></a>#elif defined(CONFIG_RTIO_BLOCK_POOL_PLACEMENT_NOCACHE)
<a id="l00289"></a>#define RTIO_BMEM __nocache static
<a id="l00290"></a>#else
<a id="l00291"></a>#define RTIO_BMEM COND_CODE_1(CONFIG_USERSPACE, (K_APP_BMEM(rtio_partition) static), (static))
<a id="l00292"></a>#endif
<a id="l00293"></a>
<a id="l00303"></a>#if CONFIG_RTIO_BLOCK_POOL_PLACEMENT_DTCM
<a id="l00304"></a>#define RTIO_DMEM Z_GENERIC_SECTION(".dtcm_data") static
<a id="l00305"></a>#elif defined(CONFIG_RTIO_BLOCK_POOL_PLACEMENT_NOCACHE)
<a id="l00306"></a>#define RTIO_DMEM __nocache_load static
<a id="l00307"></a>#else
<a id="l00308"></a>#define RTIO_DMEM COND_CODE_1(CONFIG_USERSPACE, (K_APP_DMEM(rtio_partition) static), (static))
<a id="l00309"></a>#endif
<a id="l00310"></a>
<a id="l00311"></a>/* clang-format off */
<a id="l00312"></a>/* @cond ignore */
<a id="l00313"></a>#define Z_RTIO_BLOCK_POOL_DEFINE(name, blk_sz, blk_cnt, blk_align)                                 \
<a id="l00314"></a>        RTIO_BMEM uint8_t __aligned(WB_UP(blk_align))                                              \
<a id="l00315"></a>        CONCAT(_block_pool_, name)[(blk_cnt) * WB_UP(blk_sz)];                                     \
<a id="l00316"></a>        _SYS_MEM_BLOCKS_DEFINE_WITH_EXT_BUF(name, WB_UP(blk_sz), (blk_cnt),                        \
<a id="l00317"></a>                                            CONCAT(_block_pool_, name), RTIO_DMEM)
<a id="l00318"></a>
<a id="l00319"></a>/* @endcond */
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>/* clang-format on */
<a id="l00323"></a>
<a id="l00334"></a>#define RTIO_DEFINE_WITH_MEMPOOL(name, sq_sz, cq_sz, num_blks, blk_size, balign) \
<a id="l00335"></a>        Z_RTIO_SQE_POOL_DEFINE(name##_sqe_pool, sq_sz);         \
<a id="l00336"></a>        Z_RTIO_CQE_POOL_DEFINE(name##_cqe_pool, cq_sz);                 \
<a id="l00337"></a>        Z_RTIO_BLOCK_POOL_DEFINE(name##_block_pool, blk_size, num_blks, balign); \
<a id="l00338"></a>        Z_RTIO_DEFINE(name, &amp;name##_sqe_pool, &amp;name##_cqe_pool, &amp;name##_block_pool)
<a id="l00339"></a>
<a id="l00340"></a>/* clang-format on */
<a id="l00341"></a>
<a id="l00349"></a>static inline uint32_t rtio_sqe_acquirable(struct rtio *r)
<a id="l00350"></a>{
<a id="l00351"></a>        return r-&gt;sqe_pool-&gt;pool_free;
<a id="l00352"></a>}
<a id="l00353"></a>
<a id="l00362"></a>static inline struct rtio_sqe *rtio_sqe_acquire(struct rtio *r)
<a id="l00363"></a>{
<a id="l00364"></a>        SYS_PORT_TRACING_FUNC_ENTER(rtio, sqe_acquire, r);
<a id="l00365"></a>        struct rtio_iodev_sqe *iodev_sqe = rtio_sqe_pool_alloc(r-&gt;sqe_pool);
<a id="l00366"></a>
<a id="l00367"></a>        if (iodev_sqe == NULL) {
<a id="l00368"></a>                SYS_PORT_TRACING_FUNC_EXIT(rtio, sqe_acquire, r, NULL);
<a id="l00369"></a>                return NULL;
<a id="l00370"></a>        }
<a id="l00371"></a>
<a id="l00372"></a>        mpsc_push(&amp;r-&gt;sq, &amp;iodev_sqe-&gt;q);
<a id="l00373"></a>
<a id="l00374"></a>        SYS_PORT_TRACING_FUNC_EXIT(rtio, sqe_acquire, r, &amp;iodev_sqe-&gt;sqe);
<a id="l00375"></a>        return &amp;iodev_sqe-&gt;sqe;
<a id="l00376"></a>}
<a id="l00377"></a>
<a id="l00390"></a>static inline int rtio_sqe_acquire_array(struct rtio *r, size_t n, struct rtio_sqe **sqes)
<a id="l00391"></a>{
<a id="l00392"></a>        struct rtio_iodev_sqe *iodev_sqe;
<a id="l00393"></a>        size_t i;
<a id="l00394"></a>
<a id="l00395"></a>        for (i = 0; i &lt; n; i++) {
<a id="l00396"></a>                iodev_sqe = rtio_sqe_pool_alloc(r-&gt;sqe_pool);
<a id="l00397"></a>                if (iodev_sqe == NULL) {
<a id="l00398"></a>                        break;
<a id="l00399"></a>                }
<a id="l00400"></a>                sqes[i] = &amp;iodev_sqe-&gt;sqe;
<a id="l00401"></a>        }
<a id="l00402"></a>
<a id="l00403"></a>        /* Not enough SQEs in the pool */
<a id="l00404"></a>        if (i &lt; n) {
<a id="l00405"></a>                while (i &gt; 0) {
<a id="l00406"></a>                        i--;
<a id="l00407"></a>                        iodev_sqe = CONTAINER_OF(sqes[i], struct rtio_iodev_sqe, sqe);
<a id="l00408"></a>                        rtio_sqe_pool_free(r-&gt;sqe_pool, iodev_sqe);
<a id="l00409"></a>                        sqes[i] = NULL;
<a id="l00410"></a>                }
<a id="l00411"></a>
<a id="l00412"></a>                return -ENOMEM;
<a id="l00413"></a>        }
<a id="l00414"></a>
<a id="l00415"></a>        for (i = 0; i &lt; n; i++) {
<a id="l00416"></a>                iodev_sqe = CONTAINER_OF(sqes[i], struct rtio_iodev_sqe, sqe);
<a id="l00417"></a>                mpsc_push(&amp;r-&gt;sq, &amp;iodev_sqe-&gt;q);
<a id="l00418"></a>        }
<a id="l00419"></a>
<a id="l00420"></a>        return 0;
<a id="l00421"></a>}
<a id="l00422"></a>
<a id="l00428"></a>static inline void rtio_sqe_drop_all(struct rtio *r)
<a id="l00429"></a>{
<a id="l00430"></a>        struct rtio_iodev_sqe *iodev_sqe;
<a id="l00431"></a>        struct mpsc_node *node = mpsc_pop(&amp;r-&gt;sq);
<a id="l00432"></a>
<a id="l00433"></a>        while (node != NULL) {
<a id="l00434"></a>                iodev_sqe = CONTAINER_OF(node, struct rtio_iodev_sqe, q);
<a id="l00435"></a>                rtio_sqe_pool_free(r-&gt;sqe_pool, iodev_sqe);
<a id="l00436"></a>                node = mpsc_pop(&amp;r-&gt;sq);
<a id="l00437"></a>        }
<a id="l00438"></a>}
<a id="l00439"></a>
<a id="l00443"></a>static inline struct rtio_cqe *rtio_cqe_acquire(struct rtio *r)
<a id="l00444"></a>{
<a id="l00445"></a>        SYS_PORT_TRACING_FUNC_ENTER(rtio, cqe_acquire, r);
<a id="l00446"></a>        struct rtio_cqe *cqe = rtio_cqe_pool_alloc(r-&gt;cqe_pool);
<a id="l00447"></a>
<a id="l00448"></a>        if (cqe == NULL) {
<a id="l00449"></a>                SYS_PORT_TRACING_FUNC_EXIT(rtio, cqe_acquire, r, NULL);
<a id="l00450"></a>                return NULL;
<a id="l00451"></a>        }
<a id="l00452"></a>
<a id="l00453"></a>        memset(cqe, 0, sizeof(struct rtio_cqe));
<a id="l00454"></a>
<a id="l00455"></a>        SYS_PORT_TRACING_FUNC_EXIT(rtio, cqe_acquire, r, cqe);
<a id="l00456"></a>        return cqe;
<a id="l00457"></a>}
<a id="l00458"></a>
<a id="l00475"></a>static inline int rtio_set_cqe_callback(struct rtio *r,
<a id="l00476"></a>                                        rtio_cqe_callback_t callback,
<a id="l00477"></a>                                        void *user_data)
<a id="l00478"></a>{
<a id="l00479"></a>#ifdef CONFIG_RTIO_CQE_CALLBACK
<a id="l00480"></a>        r-&gt;cqe_cb = callback;
<a id="l00481"></a>        r-&gt;cqe_cb_user_data = user_data;
<a id="l00482"></a>
<a id="l00483"></a>        return 0;
<a id="l00484"></a>#else
<a id="l00485"></a>        ARG_UNUSED(r);
<a id="l00486"></a>        ARG_UNUSED(callback);
<a id="l00487"></a>        ARG_UNUSED(user_data);
<a id="l00488"></a>
<a id="l00489"></a>        return -ENOTSUP;
<a id="l00490"></a>#endif
<a id="l00491"></a>}
<a id="l00492"></a>
<a id="l00496"></a>static inline void rtio_cqe_produce(struct rtio *r, struct rtio_cqe *cqe)
<a id="l00497"></a>{
<a id="l00498"></a>        mpsc_push(&amp;r-&gt;cq, &amp;cqe-&gt;q);
<a id="l00499"></a>}
<a id="l00500"></a>
<a id="l00512"></a>static inline struct rtio_cqe *rtio_cqe_consume(struct rtio *r)
<a id="l00513"></a>{
<a id="l00514"></a>        SYS_PORT_TRACING_FUNC_ENTER(rtio, cqe_consume, r);
<a id="l00515"></a>        struct mpsc_node *node;
<a id="l00516"></a>        struct rtio_cqe *cqe = NULL;
<a id="l00517"></a>
<a id="l00518"></a>#ifdef CONFIG_RTIO_CONSUME_SEM
<a id="l00519"></a>        if (k_sem_take(r-&gt;consume_sem, K_NO_WAIT) != 0) {
<a id="l00520"></a>                SYS_PORT_TRACING_FUNC_EXIT(rtio, cqe_consume, r, NULL);
<a id="l00521"></a>                return NULL;
<a id="l00522"></a>        }
<a id="l00523"></a>#endif
<a id="l00524"></a>
<a id="l00525"></a>        node = mpsc_pop(&amp;r-&gt;cq);
<a id="l00526"></a>        if (node == NULL) {
<a id="l00527"></a>                SYS_PORT_TRACING_FUNC_EXIT(rtio, cqe_consume, r, NULL);
<a id="l00528"></a>                return NULL;
<a id="l00529"></a>        }
<a id="l00530"></a>        cqe = CONTAINER_OF(node, struct rtio_cqe, q);
<a id="l00531"></a>
<a id="l00532"></a>        SYS_PORT_TRACING_FUNC_EXIT(rtio, cqe_consume, r, cqe);
<a id="l00533"></a>        return cqe;
<a id="l00534"></a>}
<a id="l00535"></a>
<a id="l00546"></a>static inline struct rtio_cqe *rtio_cqe_consume_block(struct rtio *r)
<a id="l00547"></a>{
<a id="l00548"></a>        struct mpsc_node *node;
<a id="l00549"></a>        struct rtio_cqe *cqe;
<a id="l00550"></a>
<a id="l00551"></a>#ifdef CONFIG_RTIO_CONSUME_SEM
<a id="l00552"></a>        k_sem_take(r-&gt;consume_sem, K_FOREVER);
<a id="l00553"></a>#endif
<a id="l00554"></a>        node = mpsc_pop(&amp;r-&gt;cq);
<a id="l00555"></a>        while (node == NULL) {
<a id="l00556"></a>                Z_SPIN_DELAY(1);
<a id="l00557"></a>                node = mpsc_pop(&amp;r-&gt;cq);
<a id="l00558"></a>        }
<a id="l00559"></a>        cqe = CONTAINER_OF(node, struct rtio_cqe, q);
<a id="l00560"></a>
<a id="l00561"></a>        return cqe;
<a id="l00562"></a>}
<a id="l00563"></a>
<a id="l00570"></a>static inline void rtio_cqe_release(struct rtio *r, struct rtio_cqe *cqe)
<a id="l00571"></a>{
<a id="l00572"></a>        SYS_PORT_TRACING_FUNC(rtio, cqe_release, r, cqe);
<a id="l00573"></a>        rtio_cqe_pool_free(r-&gt;cqe_pool, cqe);
<a id="l00574"></a>}
<a id="l00575"></a>
<a id="l00584"></a>static inline int rtio_flush_completion_queue(struct rtio *r)
<a id="l00585"></a>{
<a id="l00586"></a>        struct rtio_cqe *cqe;
<a id="l00587"></a>        int res = 0;
<a id="l00588"></a>
<a id="l00589"></a>        do {
<a id="l00590"></a>                cqe = rtio_cqe_consume(r);
<a id="l00591"></a>                if (cqe != NULL) {
<a id="l00592"></a>                        if ((cqe-&gt;result &lt; 0) &amp;&amp; (res == 0)) {
<a id="l00593"></a>                                res = cqe-&gt;result;
<a id="l00594"></a>                        }
<a id="l00595"></a>                        rtio_cqe_release(r, cqe);
<a id="l00596"></a>                }
<a id="l00597"></a>        } while (cqe != NULL);
<a id="l00598"></a>
<a id="l00599"></a>        return res;
<a id="l00600"></a>}
<a id="l00601"></a>
<a id="l00613"></a>__syscall void rtio_sqe_signal(struct rtio_sqe *sqe);
<a id="l00614"></a>
<a id="l00615"></a>static inline void z_impl_rtio_sqe_signal(struct rtio_sqe *sqe)
<a id="l00616"></a>{
<a id="l00617"></a>        struct rtio_iodev_sqe *iodev_sqe = CONTAINER_OF(sqe, struct rtio_iodev_sqe, sqe);
<a id="l00618"></a>
<a id="l00619"></a>        if (!atomic_cas(&amp;iodev_sqe-&gt;sqe.await.ok, 0, 1)) {
<a id="l00620"></a>                iodev_sqe-&gt;sqe.await.callback(iodev_sqe, iodev_sqe-&gt;sqe.await.userdata);
<a id="l00621"></a>        }
<a id="l00622"></a>}
<a id="l00623"></a>
<a id="l00630"></a>static inline uint32_t rtio_cqe_compute_flags(struct rtio_iodev_sqe *iodev_sqe)
<a id="l00631"></a>{
<a id="l00632"></a>        uint32_t flags = 0;
<a id="l00633"></a>
<a id="l00634"></a>#ifdef CONFIG_RTIO_SYS_MEM_BLOCKS
<a id="l00635"></a>        if (iodev_sqe-&gt;sqe.op == RTIO_OP_RX &amp;&amp; iodev_sqe-&gt;sqe.flags &amp; RTIO_SQE_MEMPOOL_BUFFER) {
<a id="l00636"></a>                struct rtio *r = iodev_sqe-&gt;r;
<a id="l00637"></a>                struct sys_mem_blocks *mem_pool = r-&gt;block_pool;
<a id="l00638"></a>                unsigned int blk_index = 0;
<a id="l00639"></a>                unsigned int blk_count = 0;
<a id="l00640"></a>
<a id="l00641"></a>                if (iodev_sqe-&gt;sqe.rx.buf) {
<a id="l00642"></a>                        blk_index = (iodev_sqe-&gt;sqe.rx.buf - mem_pool-&gt;buffer) &gt;&gt;
<a id="l00643"></a>                                    mem_pool-&gt;info.blk_sz_shift;
<a id="l00644"></a>                        blk_count = iodev_sqe-&gt;sqe.rx.buf_len &gt;&gt; mem_pool-&gt;info.blk_sz_shift;
<a id="l00645"></a>                }
<a id="l00646"></a>                flags = RTIO_CQE_FLAG_PREP_MEMPOOL(blk_index, blk_count);
<a id="l00647"></a>        }
<a id="l00648"></a>#else
<a id="l00649"></a>        ARG_UNUSED(iodev_sqe);
<a id="l00650"></a>#endif
<a id="l00651"></a>
<a id="l00652"></a>        return flags;
<a id="l00653"></a>}
<a id="l00654"></a>
<a id="l00670"></a>__syscall int rtio_cqe_get_mempool_buffer(const struct rtio *r, struct rtio_cqe *cqe,
<a id="l00671"></a>                                          uint8_t **buff, uint32_t *buff_len);
<a id="l00672"></a>
<a id="l00673"></a>static inline int z_impl_rtio_cqe_get_mempool_buffer(const struct rtio *r, struct rtio_cqe *cqe,
<a id="l00674"></a>                                                     uint8_t **buff, uint32_t *buff_len)
<a id="l00675"></a>{
<a id="l00676"></a>#ifdef CONFIG_RTIO_SYS_MEM_BLOCKS
<a id="l00677"></a>        if (RTIO_CQE_FLAG_GET(cqe-&gt;flags) == RTIO_CQE_FLAG_MEMPOOL_BUFFER) {
<a id="l00678"></a>                unsigned int blk_idx = RTIO_CQE_FLAG_MEMPOOL_GET_BLK_IDX(cqe-&gt;flags);
<a id="l00679"></a>                unsigned int blk_count = RTIO_CQE_FLAG_MEMPOOL_GET_BLK_CNT(cqe-&gt;flags);
<a id="l00680"></a>                uint32_t blk_size = rtio_mempool_block_size(r);
<a id="l00681"></a>
<a id="l00682"></a>                *buff_len = blk_count * blk_size;
<a id="l00683"></a>
<a id="l00684"></a>                if (blk_count &gt; 0) {
<a id="l00685"></a>                        *buff = r-&gt;block_pool-&gt;buffer + blk_idx * blk_size;
<a id="l00686"></a>
<a id="l00687"></a>                        __ASSERT_NO_MSG(*buff &gt;= r-&gt;block_pool-&gt;buffer);
<a id="l00688"></a>                        __ASSERT_NO_MSG(*buff &lt;
<a id="l00689"></a>                                r-&gt;block_pool-&gt;buffer + blk_size * r-&gt;block_pool-&gt;info.num_blocks);
<a id="l00690"></a>                } else {
<a id="l00691"></a>                        *buff = NULL;
<a id="l00692"></a>                }
<a id="l00693"></a>                return 0;
<a id="l00694"></a>        }
<a id="l00695"></a>        return -EINVAL;
<a id="l00696"></a>#else
<a id="l00697"></a>        ARG_UNUSED(r);
<a id="l00698"></a>        ARG_UNUSED(cqe);
<a id="l00699"></a>        ARG_UNUSED(buff);
<a id="l00700"></a>        ARG_UNUSED(buff_len);
<a id="l00701"></a>
<a id="l00702"></a>        return -ENOTSUP;
<a id="l00703"></a>#endif
<a id="l00704"></a>}
<a id="l00705"></a>
<a id="l00707"></a>
<a id="l00708"></a>void rtio_executor_submit(struct rtio *r);
<a id="l00709"></a>void rtio_executor_ok(struct rtio_iodev_sqe *iodev_sqe, int result);
<a id="l00710"></a>void rtio_executor_err(struct rtio_iodev_sqe *iodev_sqe, int result);
<a id="l00711"></a>
<a id="l00713"></a>
<a id="l00722"></a>static inline void rtio_iodev_sqe_ok(struct rtio_iodev_sqe *iodev_sqe, int result)
<a id="l00723"></a>{
<a id="l00724"></a>        rtio_executor_ok(iodev_sqe, result);
<a id="l00725"></a>}
<a id="l00726"></a>
<a id="l00735"></a>static inline void rtio_iodev_sqe_err(struct rtio_iodev_sqe *iodev_sqe, int result)
<a id="l00736"></a>{
<a id="l00737"></a>        rtio_executor_err(iodev_sqe, result);
<a id="l00738"></a>}
<a id="l00739"></a>
<a id="l00751"></a>static inline void rtio_cqe_submit(struct rtio *r, int result, void *userdata, uint32_t flags)
<a id="l00752"></a>{
<a id="l00753"></a>        SYS_PORT_TRACING_FUNC_ENTER(rtio, cqe_submit, r, result, flags);
<a id="l00754"></a>        struct rtio_cqe *cqe = rtio_cqe_acquire(r);
<a id="l00755"></a>
<a id="l00756"></a>        if (cqe == NULL) {
<a id="l00757"></a>                atomic_inc(&amp;r-&gt;xcqcnt);
<a id="l00758"></a>        } else {
<a id="l00759"></a>                cqe-&gt;result = result;
<a id="l00760"></a>                cqe-&gt;userdata = userdata;
<a id="l00761"></a>                cqe-&gt;flags = flags;
<a id="l00762"></a>                rtio_cqe_produce(r, cqe);
<a id="l00763"></a>#ifdef CONFIG_RTIO_CONSUME_SEM
<a id="l00764"></a>                k_sem_give(r-&gt;consume_sem);
<a id="l00765"></a>#endif
<a id="l00766"></a>#ifdef CONFIG_RTIO_CQE_CALLBACK
<a id="l00767"></a>                if (r-&gt;cqe_cb != NULL) {
<a id="l00768"></a>                        r-&gt;cqe_cb(r, r-&gt;cqe_cb_user_data);
<a id="l00769"></a>                }
<a id="l00770"></a>#endif
<a id="l00771"></a>        }
<a id="l00772"></a>
<a id="l00773"></a>        /* atomic_t isn't guaranteed to wrap correctly as it could be signed, so
<a id="l00774"></a>         * we must resort to a cas loop.
<a id="l00775"></a>         */
<a id="l00776"></a>        atomic_t val, new_val;
<a id="l00777"></a>
<a id="l00778"></a>        do {
<a id="l00779"></a>                val = atomic_get(&amp;r-&gt;cq_count);
<a id="l00780"></a>                new_val = (atomic_t)((uintptr_t)val + 1);
<a id="l00781"></a>        } while (!atomic_cas(&amp;r-&gt;cq_count, val, new_val));
<a id="l00782"></a>
<a id="l00783"></a>#ifdef CONFIG_RTIO_SUBMIT_SEM
<a id="l00784"></a>        if (r-&gt;submit_count &gt; 0) {
<a id="l00785"></a>                r-&gt;submit_count--;
<a id="l00786"></a>                if (r-&gt;submit_count == 0) {
<a id="l00787"></a>                        k_sem_give(r-&gt;submit_sem);
<a id="l00788"></a>                }
<a id="l00789"></a>        }
<a id="l00790"></a>#endif
<a id="l00791"></a>        SYS_PORT_TRACING_FUNC_EXIT(rtio, cqe_submit, r);
<a id="l00792"></a>}
<a id="l00793"></a>
<a id="l00794"></a>#define __RTIO_MEMPOOL_GET_NUM_BLKS(num_bytes, blk_size) (((num_bytes) + (blk_size)-1) / (blk_size))
<a id="l00795"></a>
<a id="l00808"></a>static inline int rtio_sqe_rx_buf(const struct rtio_iodev_sqe *iodev_sqe, uint32_t min_buf_len,
<a id="l00809"></a>                                  uint32_t max_buf_len, uint8_t **buf, uint32_t *buf_len)
<a id="l00810"></a>{
<a id="l00811"></a>        struct rtio_sqe *sqe = (struct rtio_sqe *)&amp;iodev_sqe-&gt;sqe;
<a id="l00812"></a>
<a id="l00813"></a>#ifdef CONFIG_RTIO_SYS_MEM_BLOCKS
<a id="l00814"></a>        if (sqe-&gt;op == RTIO_OP_RX &amp;&amp; sqe-&gt;flags &amp; RTIO_SQE_MEMPOOL_BUFFER) {
<a id="l00815"></a>                struct rtio *r = iodev_sqe-&gt;r;
<a id="l00816"></a>
<a id="l00817"></a>                if (sqe-&gt;rx.buf != NULL) {
<a id="l00818"></a>                        if (sqe-&gt;rx.buf_len &lt; min_buf_len) {
<a id="l00819"></a>                                return -ENOMEM;
<a id="l00820"></a>                        }
<a id="l00821"></a>                        *buf = sqe-&gt;rx.buf;
<a id="l00822"></a>                        *buf_len = sqe-&gt;rx.buf_len;
<a id="l00823"></a>                        return 0;
<a id="l00824"></a>                }
<a id="l00825"></a>
<a id="l00826"></a>                int rc = rtio_block_pool_alloc(r, min_buf_len, max_buf_len, buf, buf_len);
<a id="l00827"></a>                if (rc == 0) {
<a id="l00828"></a>                        sqe-&gt;rx.buf = *buf;
<a id="l00829"></a>                        sqe-&gt;rx.buf_len = *buf_len;
<a id="l00830"></a>                        return 0;
<a id="l00831"></a>                }
<a id="l00832"></a>
<a id="l00833"></a>                return -ENOMEM;
<a id="l00834"></a>        }
<a id="l00835"></a>#else
<a id="l00836"></a>        ARG_UNUSED(max_buf_len);
<a id="l00837"></a>#endif
<a id="l00838"></a>
<a id="l00839"></a>        if (sqe-&gt;rx.buf_len &lt; min_buf_len) {
<a id="l00840"></a>                return -ENOMEM;
<a id="l00841"></a>        }
<a id="l00842"></a>
<a id="l00843"></a>        *buf = sqe-&gt;rx.buf;
<a id="l00844"></a>        *buf_len = sqe-&gt;rx.buf_len;
<a id="l00845"></a>        return 0;
<a id="l00846"></a>}
<a id="l00847"></a>
<a id="l00862"></a>__syscall void rtio_release_buffer(struct rtio *r, void *buff, uint32_t buff_len);
<a id="l00863"></a>
<a id="l00864"></a>static inline void z_impl_rtio_release_buffer(struct rtio *r, void *buff, uint32_t buff_len)
<a id="l00865"></a>{
<a id="l00866"></a>#ifdef CONFIG_RTIO_SYS_MEM_BLOCKS
<a id="l00867"></a>        if (r == NULL || buff == NULL || r-&gt;block_pool == NULL || buff_len == 0) {
<a id="l00868"></a>                return;
<a id="l00869"></a>        }
<a id="l00870"></a>
<a id="l00871"></a>        rtio_block_pool_free(r, buff, buff_len);
<a id="l00872"></a>#else
<a id="l00873"></a>        ARG_UNUSED(r);
<a id="l00874"></a>        ARG_UNUSED(buff);
<a id="l00875"></a>        ARG_UNUSED(buff_len);
<a id="l00876"></a>#endif
<a id="l00877"></a>}
<a id="l00878"></a>
<a id="l00885"></a>static inline void rtio_access_grant(struct rtio *r, struct k_thread *t)
<a id="l00886"></a>{
<a id="l00887"></a>        k_object_access_grant(r, t);
<a id="l00888"></a>
<a id="l00889"></a>#ifdef CONFIG_RTIO_SUBMIT_SEM
<a id="l00890"></a>        k_object_access_grant(r-&gt;submit_sem, t);
<a id="l00891"></a>#endif
<a id="l00892"></a>
<a id="l00893"></a>#ifdef CONFIG_RTIO_CONSUME_SEM
<a id="l00894"></a>        k_object_access_grant(r-&gt;consume_sem, t);
<a id="l00895"></a>#endif
<a id="l00896"></a>
<a id="l00897"></a>#ifdef CONFIG_RTIO_OP_DELAY
<a id="l00898"></a>        /* Delay submissions are dispatched to the shared timeout iodev, so a thread
<a id="l00899"></a>         * allowed to use this context must also be able to reference it.
<a id="l00900"></a>         */
<a id="l00901"></a>        k_object_access_grant(&amp;rtio_timeout_iodev, t);
<a id="l00902"></a>#endif
<a id="l00903"></a>}
<a id="l00904"></a>
<a id="l00905"></a>
<a id="l00912"></a>static inline void rtio_access_revoke(struct rtio *r, struct k_thread *t)
<a id="l00913"></a>{
<a id="l00914"></a>        k_object_access_revoke(r, t);
<a id="l00915"></a>
<a id="l00916"></a>#ifdef CONFIG_RTIO_SUBMIT_SEM
<a id="l00917"></a>        k_object_access_revoke(r-&gt;submit_sem, t);
<a id="l00918"></a>#endif
<a id="l00919"></a>
<a id="l00920"></a>#ifdef CONFIG_RTIO_CONSUME_SEM
<a id="l00921"></a>        k_object_access_revoke(r-&gt;consume_sem, t);
<a id="l00922"></a>#endif
<a id="l00923"></a>
<a id="l00924"></a>#ifdef CONFIG_RTIO_OP_DELAY
<a id="l00925"></a>        k_object_access_revoke(&amp;rtio_timeout_iodev, t);
<a id="l00926"></a>#endif
<a id="l00927"></a>}
<a id="l00928"></a>
<a id="l00939"></a>__syscall int rtio_sqe_cancel(struct rtio_sqe *sqe);
<a id="l00940"></a>
<a id="l00941"></a>static inline int z_impl_rtio_sqe_cancel(struct rtio_sqe *sqe)
<a id="l00942"></a>{
<a id="l00943"></a>        SYS_PORT_TRACING_FUNC(rtio, sqe_cancel, sqe);
<a id="l00944"></a>        struct rtio_iodev_sqe *iodev_sqe = CONTAINER_OF(sqe, struct rtio_iodev_sqe, sqe);
<a id="l00945"></a>
<a id="l00946"></a>        do {
<a id="l00947"></a>                iodev_sqe-&gt;sqe.flags |= RTIO_SQE_CANCELED;
<a id="l00948"></a>                iodev_sqe = rtio_iodev_sqe_next(iodev_sqe);
<a id="l00949"></a>        } while (iodev_sqe != NULL);
<a id="l00950"></a>
<a id="l00951"></a>        return 0;
<a id="l00952"></a>}
<a id="l00953"></a>
<a id="l00969"></a>__syscall int rtio_sqe_copy_in_get_handles(struct rtio *r, const struct rtio_sqe *sqes,
<a id="l00970"></a>                                           struct rtio_sqe **handle, size_t sqe_count);
<a id="l00971"></a>
<a id="l00972"></a>static inline int z_impl_rtio_sqe_copy_in_get_handles(struct rtio *r, const struct rtio_sqe *sqes,
<a id="l00973"></a>                                                      struct rtio_sqe **handle,
<a id="l00974"></a>                                                      size_t sqe_count)
<a id="l00975"></a>{
<a id="l00976"></a>        struct rtio_sqe *sqe;
<a id="l00977"></a>        uint32_t acquirable = rtio_sqe_acquirable(r);
<a id="l00978"></a>
<a id="l00979"></a>        if (acquirable &lt; sqe_count) {
<a id="l00980"></a>                return -ENOMEM;
<a id="l00981"></a>        }
<a id="l00982"></a>
<a id="l00983"></a>        for (unsigned long i = 0; i &lt; sqe_count; i++) {
<a id="l00984"></a>                sqe = rtio_sqe_acquire(r);
<a id="l00985"></a>                __ASSERT_NO_MSG(sqe != NULL);
<a id="l00986"></a>                if (handle != NULL &amp;&amp; i == 0) {
<a id="l00987"></a>                        *handle = sqe;
<a id="l00988"></a>                }
<a id="l00989"></a>                *sqe = sqes[i];
<a id="l00990"></a>        }
<a id="l00991"></a>
<a id="l00992"></a>        return 0;
<a id="l00993"></a>}
<a id="l00994"></a>
<a id="l01011"></a>static inline int rtio_sqe_copy_in(struct rtio *r, const struct rtio_sqe *sqes, size_t sqe_count)
<a id="l01012"></a>{
<a id="l01013"></a>        return rtio_sqe_copy_in_get_handles(r, sqes, NULL, sqe_count);
<a id="l01014"></a>}
<a id="l01015"></a>
<a id="l01031"></a>__syscall int rtio_cqe_copy_out(struct rtio *r,
<a id="l01032"></a>                                struct rtio_cqe *cqes,
<a id="l01033"></a>                                size_t cqe_count,
<a id="l01034"></a>                                k_timeout_t timeout);
<a id="l01035"></a>static inline int z_impl_rtio_cqe_copy_out(struct rtio *r,
<a id="l01036"></a>                                           struct rtio_cqe *cqes,
<a id="l01037"></a>                                           size_t cqe_count,
<a id="l01038"></a>                                           k_timeout_t timeout)
<a id="l01039"></a>{
<a id="l01040"></a>        size_t copied = 0;
<a id="l01041"></a>        struct rtio_cqe *cqe;
<a id="l01042"></a>        k_timepoint_t end = sys_timepoint_calc(timeout);
<a id="l01043"></a>
<a id="l01044"></a>        do {
<a id="l01045"></a>                cqe = K_TIMEOUT_EQ(timeout, K_FOREVER) ? rtio_cqe_consume_block(r)
<a id="l01046"></a>                                                       : rtio_cqe_consume(r);
<a id="l01047"></a>                if (cqe == NULL) {
<a id="l01048"></a>                        Z_SPIN_DELAY(25);
<a id="l01049"></a>                        continue;
<a id="l01050"></a>                }
<a id="l01051"></a>                cqes[copied++] = *cqe;
<a id="l01052"></a>                rtio_cqe_release(r, cqe);
<a id="l01053"></a>        } while (copied &lt; cqe_count &amp;&amp; !sys_timepoint_expired(end));
<a id="l01054"></a>
<a id="l01055"></a>        return copied;
<a id="l01056"></a>}
<a id="l01057"></a>
<a id="l01073"></a>__syscall int rtio_submit(struct rtio *r, uint32_t wait_count);
<a id="l01074"></a>
<a id="l01075"></a>#ifdef CONFIG_RTIO_SUBMIT_SEM
<a id="l01076"></a>static inline int z_impl_rtio_submit(struct rtio *r, uint32_t wait_count)
<a id="l01077"></a>{
<a id="l01078"></a>        SYS_PORT_TRACING_FUNC_ENTER(rtio, submit, r, wait_count);
<a id="l01079"></a>        int res = 0;
<a id="l01080"></a>
<a id="l01081"></a>        if (wait_count &gt; 0) {
<a id="l01082"></a>                __ASSERT(!k_is_in_isr(),
<a id="l01083"></a>                         "expected rtio submit with wait count to be called from a thread");
<a id="l01084"></a>
<a id="l01085"></a>                k_sem_reset(r-&gt;submit_sem);
<a id="l01086"></a>                r-&gt;submit_count = wait_count;
<a id="l01087"></a>        }
<a id="l01088"></a>
<a id="l01089"></a>        rtio_executor_submit(r);
<a id="l01090"></a>
<a id="l01091"></a>        if (wait_count &gt; 0) {
<a id="l01092"></a>                res = k_sem_take(r-&gt;submit_sem, K_FOREVER);
<a id="l01093"></a>                __ASSERT(res == 0,
<a id="l01094"></a>                         "semaphore was reset or timed out while waiting on completions!");
<a id="l01095"></a>        }
<a id="l01096"></a>
<a id="l01097"></a>        SYS_PORT_TRACING_FUNC_EXIT(rtio, submit, r);
<a id="l01098"></a>        return res;
<a id="l01099"></a>}
<a id="l01100"></a>#else
<a id="l01101"></a>static inline int z_impl_rtio_submit(struct rtio *r, uint32_t wait_count)
<a id="l01102"></a>{
<a id="l01103"></a>
<a id="l01104"></a>        SYS_PORT_TRACING_FUNC_ENTER(rtio, submit, r, wait_count);
<a id="l01105"></a>        int res = 0;
<a id="l01106"></a>        uintptr_t cq_count = (uintptr_t)atomic_get(&amp;r-&gt;cq_count);
<a id="l01107"></a>        uintptr_t cq_complete_count = cq_count + wait_count;
<a id="l01108"></a>        bool wraps = cq_complete_count &lt; cq_count;
<a id="l01109"></a>
<a id="l01110"></a>        rtio_executor_submit(r);
<a id="l01111"></a>
<a id="l01112"></a>        if (wraps) {
<a id="l01113"></a>                while ((uintptr_t)atomic_get(&amp;r-&gt;cq_count) &gt;= cq_count) {
<a id="l01114"></a>                        Z_SPIN_DELAY(10);
<a id="l01115"></a>                        k_yield();
<a id="l01116"></a>                }
<a id="l01117"></a>        }
<a id="l01118"></a>
<a id="l01119"></a>        while ((uintptr_t)atomic_get(&amp;r-&gt;cq_count) &lt; cq_complete_count) {
<a id="l01120"></a>                Z_SPIN_DELAY(10);
<a id="l01121"></a>                k_yield();
<a id="l01122"></a>        }
<a id="l01123"></a>
<a id="l01124"></a>        SYS_PORT_TRACING_FUNC_EXIT(rtio, submit, r);
<a id="l01125"></a>        return res;
<a id="l01126"></a>}
<a id="l01127"></a>#endif /* CONFIG_RTIO_SUBMIT_SEM */
<a id="l01128"></a>
<a id="l01132"></a>struct rtio_pool {
<a id="l01134"></a>        size_t pool_size;
<a id="l01135"></a>
<a id="l01137"></a>        struct rtio **contexts;
<a id="l01138"></a>
<a id="l01140"></a>        atomic_t *used;
<a id="l01141"></a>};
<a id="l01142"></a>
<a id="l01151"></a>__syscall struct rtio *rtio_pool_acquire(struct rtio_pool *pool);
<a id="l01152"></a>
<a id="l01153"></a>static inline struct rtio *z_impl_rtio_pool_acquire(struct rtio_pool *pool)
<a id="l01154"></a>{
<a id="l01155"></a>        struct rtio *r = NULL;
<a id="l01156"></a>
<a id="l01157"></a>        for (size_t i = 0; i &lt; pool-&gt;pool_size; i++) {
<a id="l01158"></a>                if (atomic_test_and_set_bit(pool-&gt;used, i) == 0) {
<a id="l01159"></a>                        r = pool-&gt;contexts[i];
<a id="l01160"></a>                        break;
<a id="l01161"></a>                }
<a id="l01162"></a>        }
<a id="l01163"></a>
<a id="l01164"></a>        if (r != NULL) {
<a id="l01165"></a>                rtio_access_grant(r, k_current_get());
<a id="l01166"></a>        }
<a id="l01167"></a>
<a id="l01168"></a>        return r;
<a id="l01169"></a>}
<a id="l01170"></a>
<a id="l01177"></a>__syscall void rtio_pool_release(struct rtio_pool *pool, struct rtio *r);
<a id="l01178"></a>
<a id="l01179"></a>static inline void z_impl_rtio_pool_release(struct rtio_pool *pool, struct rtio *r)
<a id="l01180"></a>{
<a id="l01181"></a>
<a id="l01182"></a>        if (k_is_user_context()) {
<a id="l01183"></a>                rtio_access_revoke(r, k_current_get());
<a id="l01184"></a>        }
<a id="l01185"></a>
<a id="l01186"></a>        for (size_t i = 0; i &lt; pool-&gt;pool_size; i++) {
<a id="l01187"></a>                if (pool-&gt;contexts[i] == r) {
<a id="l01188"></a>                        atomic_clear_bit(pool-&gt;used, i);
<a id="l01189"></a>                        break;
<a id="l01190"></a>                }
<a id="l01191"></a>        }
<a id="l01192"></a>}
<a id="l01193"></a>
<a id="l01194"></a>/* clang-format off */
<a id="l01195"></a>
<a id="l01197"></a>
<a id="l01198"></a>#define Z_RTIO_POOL_NAME_N(n, name)                                             \
<a id="l01199"></a>        name##_##n
<a id="l01200"></a>
<a id="l01201"></a>#define Z_RTIO_POOL_DEFINE_N(n, name, sq_sz, cq_sz)                             \
<a id="l01202"></a>        RTIO_DEFINE(Z_RTIO_POOL_NAME_N(n, name), sq_sz, cq_sz)
<a id="l01203"></a>
<a id="l01204"></a>#define Z_RTIO_POOL_REF_N(n, name)                                              \
<a id="l01205"></a>        &amp;Z_RTIO_POOL_NAME_N(n, name)
<a id="l01206"></a>
<a id="l01208"></a>
<a id="l01217"></a>#define RTIO_POOL_DEFINE(name, pool_sz, sq_sz, cq_sz)                           \
<a id="l01218"></a>        LISTIFY(pool_sz, Z_RTIO_POOL_DEFINE_N, (;), name, sq_sz, cq_sz);        \
<a id="l01219"></a>        static struct rtio *name##_contexts[] = {                               \
<a id="l01220"></a>                LISTIFY(pool_sz, Z_RTIO_POOL_REF_N, (,), name)                  \
<a id="l01221"></a>        };                                                                      \
<a id="l01222"></a>        ATOMIC_DEFINE(name##_used, pool_sz);                                    \
<a id="l01223"></a>        STRUCT_SECTION_ITERABLE(rtio_pool, name) = {                            \
<a id="l01224"></a>                .pool_size = pool_sz,                                           \
<a id="l01225"></a>                .contexts = name##_contexts,                                    \
<a id="l01226"></a>                .used = name##_used,                                            \
<a id="l01227"></a>        }
<a id="l01228"></a>
<a id="l01229"></a>/* clang-format on */
<a id="l01230"></a>
<a id="l01234"></a>
<a id="l01235"></a>#ifdef __cplusplus
<a id="l01236"></a>}
<a id="l01237"></a>#endif
<a id="l01238"></a>
<a id="l01239"></a>#include &lt;zephyr/syscalls/rtio.h&gt;
<a id="l01240"></a>
<a id="l01241"></a>#endif /* ZEPHYR_INCLUDE_RTIO_RTIO_H_ */
</code></pre>

## 3.2\_可见注释译文（Comments）

1. 版权属于Intel Corporation（2022年）以及Infineon Technologies AG或其关联公司（2026年）；保留全部权利，许可证为Apache-2.0。原始SPDX记录完整保留。

2. 等待信号量（Semaphore）：调用submit时，可能挂起调用线程，以等待一定数量的完成事件。

3. 等待信号量（Semaphore）：从完成队列取出事件时，可能挂起调用线程，以等待一定数量的完成事件。

4. 内存块池（Memory Block Pool）。

5. 完成队列事件回调（CQE Callback）。

6. 完成队列事件回调的用户数据（User Data）。

7. Doxygen条件隐藏区开始：`@cond ignore`。

8. Doxygen条件隐藏区结束：`@endcond`。

9. 并非每个上下文都有内存块池；没有块池时，块大小可能返回0。

10. 不要尝试重新格式化这些宏。

11. 关闭clang-format自动格式化。

12. Doxygen条件隐藏区开始：`@cond ignore`。

13. Doxygen条件隐藏区结束：`@endcond`。

14. 恢复clang-format自动格式化。

15. 恢复clang-format自动格式化。

16. 池中没有足够的SQE。

17. `atomic_t`可能是有符号类型，不能保证正确回绕，因此必须使用比较并交换（Compare-and-Swap，CAS）循环。

18. 延时提交分派给共享的超时IODEV，因此获准使用此上下文的线程也必须能够引用该设备。

19. `CONFIG_RTIO_SUBMIT_SEM`条件编译区结束。

20. 关闭clang-format自动格式化。

21. 恢复clang-format自动格式化。

22. 头文件保护宏`ZEPHYR_INCLUDE_RTIO_RTIO_H_`结束。

## 3.3\_原页符号提示（Symbol Descriptions）

### `app_memdomain.h`

符号定位：[app_memdomain.h](../memory_domain_reference/P009_应用内存域头文件参考.md)。

### `atomic.h`

原子操作（Atomic Operations）API头文件。

符号定位：[atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)。

### `cqe.h`

RTIO完成队列事件（Completion Queue Events）及相关函数。

符号定位：[cqe.h](../rtio_headers_reference/P003_RTIO完成事件头文件参考.md)。

### `device.h`

Zephyr设备模型（Device Model）的API和宏。

符号定位：[device.h](../device_reference/P007_设备模型头文件参考.md)。

### `atomic_t`

```c
long atomic_t
```

原子整数变量（Atomic Integer Variable）。

定义位置（Definition）：atomic_types.h:34。

符号定位：[atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)。

### `atomic_clear_bit`

```c
static void atomic_clear_bit(atomic_t *target, int bit)
```

以原子方式清除一个位。

定义位置（Definition）：atomic.h:227。

符号定位：[atomic_clear_bit](../atomic_reference/P001_原子操作公共接口.md#ga1c1693d524c49d11fd32b323a39d718e)。

### `atomic_get`

```c
atomic_val_t atomic_get(const atomic_t *target)
```

原子读取（Atomic Get）。

符号定位：[atomic_get](../atomic_reference/P001_原子操作公共接口.md#ga33bb426a17535bd1022895a7e44b32fa)。

### `atomic_test_and_set_bit`

```c
static bool atomic_test_and_set_bit(atomic_t *target, int bit)
```

以原子方式设置并测试一个位。

定义位置（Definition）：atomic.h:181。

符号定位：[atomic_test_and_set_bit](../atomic_reference/P001_原子操作公共接口.md#ga7ff45e13aa5f8be5d7a550e49f5c720b)。

### `atomic_inc`

```c
atomic_val_t atomic_inc(atomic_t *target)
```

原子递增（Atomic Increment）。

符号定位：[atomic_inc](../atomic_reference/P001_原子操作公共接口.md#gaae47a9cbe5a6534967b417f602b37ac2)。

### `atomic_cas`

```c
bool atomic_cas(atomic_t *target, atomic_val_t old_value, atomic_val_t new_value)
```

原子比较并设置（Atomic Compare-and-Set）。

符号定位：[atomic_cas](../atomic_reference/P001_原子操作公共接口.md#gab879da5aa1ffcc317adc664c016586f7)。

### `K_FOREVER`

```c
#define K_FOREVER
```

生成无限等待的超时值。

定义位置（Definition）：kernel.h:1712。

符号定位：[K_FOREVER](../timer_reference/P086_系统时钟公共接口.md#ga0bb4b83f0222193b21a8910311bab0ca)。

### `K_NO_WAIT`

```c
#define K_NO_WAIT
```

生成不等待的超时值。

定义位置（Definition）：kernel.h:1602。

符号定位：[K_NO_WAIT](../timer_reference/P086_系统时钟公共接口.md#ga3d9541cfe2e8395af66d186efa77362f)。

### `sys_timepoint_calc`

```c
k_timepoint_t sys_timepoint_calc(k_timeout_t timeout)
```

计算时间点（Timepoint）值。

符号定位：[sys_timepoint_calc](../timer_reference/P086_系统时钟公共接口.md#ga509cf4599c1f162c97540743e8c21d33)。

### `sys_timepoint_expired`

```c
static bool sys_timepoint_expired(k_timepoint_t timepoint)
```

指示时间点是否已经到期。

定义位置（Definition）：clock.h:386。

符号定位：[sys_timepoint_expired](../timer_reference/P086_系统时钟公共接口.md#ga87d0d7a0f7bcdcc8c4909962eac12985)。

### `K_TIMEOUT_EQ`

```c
#define K_TIMEOUT_EQ(a, b)
```

比较两个超时值是否相等。

定义位置（Definition）：clock.h:80。

符号定位：[K_TIMEOUT_EQ](../timer_reference/P086_系统时钟公共接口.md#ga9abf00b34e16ab7ad0883603b6778b1b)。

### `k_is_in_isr`

```c
bool k_is_in_isr(void)
```

判断代码是否运行在中断级别（Interrupt Level）。

符号定位：[k_is_in_isr](../fatal_irq_reference/P007_中断服务接口.md#ga8482b0dd2283d12677a9ebe321667d16)。

### `sys_mem_blocks_free_contiguous`

```c
int sys_mem_blocks_free_contiguous(sys_mem_blocks_t *mem_block, void *block, size_t count)
```

释放多个连续内存块。

符号定位：[sys_mem_blocks_free_contiguous](../memblocks_reference/P001_内存块分配公共接口.md#ga39e7f8dfe3bda8eabc2372f9a1e87342)。

### `sys_mem_blocks_alloc_contiguous`

```c
int sys_mem_blocks_alloc_contiguous(sys_mem_blocks_t *mem_block, size_t count, void **out_block)
```

分配一组连续内存块。

符号定位：[sys_mem_blocks_alloc_contiguous](../memblocks_reference/P001_内存块分配公共接口.md#ga72614d0c120f40209837b77d0333bb23)。

### `mpsc_push`

```c
static ALWAYS_INLINE void mpsc_push(struct mpsc *q, struct mpsc_node *n)
```

压入一个节点（Node）。

定义位置（Definition）：mpsc_lockfree.h:126。

符号定位：[mpsc_push](../intercore_reference/P158_MPSC无锁队列接口.md#ga403add133841ef88e10d74141e782b37)。

### `mpsc_pop`

```c
static struct mpsc_node * mpsc_pop(struct mpsc *q)
```

从链表中弹出一个节点。

定义位置（Definition）：mpsc_lockfree.h:145。

符号定位：[mpsc_pop](../intercore_reference/P158_MPSC无锁队列接口.md#ga823ec37b84ac43e46167aac954bce9d7)。

### `RTIO_CQE_FLAG_MEMPOOL_GET_BLK_CNT`

```c
#define RTIO_CQE_FLAG_MEMPOOL_GET_BLK_CNT(flags)
```

从内存池标志中取得块数。

定义位置（Definition）：cqe.h:70。

符号定位：[RTIO_CQE_FLAG_MEMPOOL_GET_BLK_CNT](../rtio_model_reference/P008_RTIO完成事件标志.md#ga087465f866d417d5332602bb582cc1a7)。

### `RTIO_CQE_FLAG_MEMPOOL_GET_BLK_IDX`

```c
#define RTIO_CQE_FLAG_MEMPOOL_GET_BLK_IDX(flags)
```

从内存池标志中取得块索引。

定义位置（Definition）：cqe.h:62。

符号定位：[RTIO_CQE_FLAG_MEMPOOL_GET_BLK_IDX](../rtio_model_reference/P008_RTIO完成事件标志.md#ga0b5f3f7e7be472ecf87bd2b08c1888da)。

### `RTIO_CQE_FLAG_MEMPOOL_BUFFER`

```c
#define RTIO_CQE_FLAG_MEMPOOL_BUFFER
```

该条目的缓冲区由RTIO内存池分配。

定义位置（Definition）：cqe.h:46。

符号定位：[RTIO_CQE_FLAG_MEMPOOL_BUFFER](../rtio_model_reference/P008_RTIO完成事件标志.md#ga0f212500447a5e37e225a6997953b609)。

### `RTIO_CQE_FLAG_PREP_MEMPOOL`

```c
#define RTIO_CQE_FLAG_PREP_MEMPOOL(blk_idx, blk_cnt)
```

为内存池读操作准备CQE标志。

定义位置（Definition）：cqe.h:79。

符号定位：[RTIO_CQE_FLAG_PREP_MEMPOOL](../rtio_model_reference/P008_RTIO完成事件标志.md#ga28b3a5661248b6b3763aab47417114d6)。

### `RTIO_CQE_FLAG_GET`

```c
#define RTIO_CQE_FLAG_GET(flags)
```

从CQE标志值中取得标志位。

定义位置（Definition）：cqe.h:54。

符号定位：[RTIO_CQE_FLAG_GET](../rtio_model_reference/P008_RTIO完成事件标志.md#gaef64ea020a20ac22a0edcb6eca032efc)。

### `RTIO_OP_RX`

```c
#define RTIO_OP_RX
```

执行接收（读取）的操作。

定义位置（Definition）：sqe.h:145。

符号定位：[RTIO_OP_RX](../rtio_model_reference/P009_RTIO操作码.md#gafeb05c351207cd1638fa78f6607e1a4a)。

### `RTIO_SQE_MEMPOOL_BUFFER`

```c
#define RTIO_SQE_MEMPOOL_BUFFER
```

缓冲区应由RTIO内存池分配。

定义位置（Definition）：sqe.h:106。

符号定位：[RTIO_SQE_MEMPOOL_BUFFER](../rtio_model_reference/P010_RTIO提交事件标志.md#ga2802b46584220afffa0e959e149d5a4d)。

### `RTIO_SQE_CANCELED`

```c
#define RTIO_SQE_CANCELED
```

如果可能，不应执行该SQE。

定义位置（Definition）：sqe.h:114。

符号定位：[RTIO_SQE_CANCELED](../rtio_model_reference/P010_RTIO提交事件标志.md#ga7f7f9b038ab8409f271b1aebc1b95ee6)。

### `rtio_pool_release`

```c
void rtio_pool_release(struct rtio_pool *pool, struct rtio *r)
```

将RTIO上下文（Context）归还到池中。

符号定位：[rtio_pool_release](P001_RTIO公共接口.md#ga05e24d59485f71cc0126d44abbe8cf2b)。

### `rtio_sqe_acquirable`

```c
static uint32_t rtio_sqe_acquirable(struct rtio *r)
```

可获取的提交队列事件数。

定义位置（Definition）：rtio.h:349。

符号定位：[rtio_sqe_acquirable](P001_RTIO公共接口.md#ga1f4fb7bccbaae08a94387e4b11275a78)。

### `rtio_pool_acquire`

```c
struct rtio * rtio_pool_acquire(struct rtio_pool *pool)
```

从池中取得一个RTIO上下文（Context）。

符号定位：[rtio_pool_acquire](P001_RTIO公共接口.md#ga37c94f84cfce3810fd598040aba3841e)。

### `rtio_mempool_block_size`

```c
static size_t rtio_mempool_block_size(const struct rtio *r)
```

获取RTIO上下文的内存池块大小（Memory Pool Block Size）。

定义位置（Definition）：rtio.h:175。

符号定位：[rtio_mempool_block_size](P001_RTIO公共接口.md#ga4213be028b0a1264daaa0d30c4c2d089)。

### `rtio_cqe_submit`

```c
static void rtio_cqe_submit(struct rtio *r, int result, void *userdata, uint32_t flags)
```

使用给定结果和用户数据（User Data）提交一个完成队列事件（CQE）。

定义位置（Definition）：rtio.h:751。

符号定位：[rtio_cqe_submit](P001_RTIO公共接口.md#ga4abc221d5a90ab882000a72caa0ebd0f)。

### `rtio_release_buffer`

```c
void rtio_release_buffer(struct rtio *r, void *buff, uint32_t buff_len)
```

释放由RTIO内存池（Memory Pool）分配的内存。

符号定位：[rtio_release_buffer](P001_RTIO公共接口.md#ga6530bf56ccbab046a362a6448f941609)。

### `rtio_sqe_copy_in`

```c
static int rtio_sqe_copy_in(struct rtio *r, const struct rtio_sqe *sqes, size_t sqe_count)
```

将SQE数组复制到队列中。

定义位置（Definition）：rtio.h:1011。

符号定位：[rtio_sqe_copy_in](P001_RTIO公共接口.md#ga65e351af0a16dcf504a51ef4eb9316c7)。

### `rtio_cqe_callback_t`

```c
void(* rtio_cqe_callback_t)(struct rtio *r, void *user_data)
```

RTIO完成队列事件回调（Completion Queue Event Callback）。

定义位置（Definition）：rtio.h:70。

符号定位：[rtio_cqe_callback_t](P001_RTIO公共接口.md#ga6adaa4d7ef1fa8054000d8d9b8e634bd)。

### `rtio_cqe_produce`

```c
static void rtio_cqe_produce(struct rtio *r, struct rtio_cqe *cqe)
```

如果可用，产生一个完成队列事件（CQE）。

定义位置（Definition）：rtio.h:496。

符号定位：[rtio_cqe_produce](P001_RTIO公共接口.md#ga6f55202adeca60aed0343a7a0dcab071)。

### `rtio_cqe_compute_flags`

```c
static uint32_t rtio_cqe_compute_flags(struct rtio_iodev_sqe *iodev_sqe)
```

根据`rtio_iodev_sqe`条目计算CQE标志。

定义位置（Definition）：rtio.h:630。

符号定位：[rtio_cqe_compute_flags](P001_RTIO公共接口.md#ga75661c8c6c94a0ac6254cec674b478c8)。

### `rtio_sqe_copy_in_get_handles`

```c
int rtio_sqe_copy_in_get_handles(struct rtio *r, const struct rtio_sqe *sqes, struct rtio_sqe **handle, size_t sqe_count)
```

将SQE数组复制到队列中，并取回生成的句柄（Handles）。

符号定位：[rtio_sqe_copy_in_get_handles](P001_RTIO公共接口.md#ga830863e6c8d9b96f4c473a038cab8f8c)。

### `rtio_partition`

```c
struct k_mem_partition rtio_partition
```

与全部RTIO上下文信息关联的内存分区（Memory Partition）。

符号定位：[rtio_partition](P001_RTIO公共接口.md#ga86a38086dd85150ab6e479d73db1c6d1)。

### `rtio_sqe_acquire`

```c
static struct rtio_sqe * rtio_sqe_acquire(struct rtio *r)
```

如果可用，获取一个提交队列事件（SQE）。

定义位置（Definition）：rtio.h:362。

符号定位：[rtio_sqe_acquire](P001_RTIO公共接口.md#ga8b47c954d15a334621def53acceb6799)。

### `rtio_sqe_drop_all`

```c
static void rtio_sqe_drop_all(struct rtio *r)
```

丢弃先前获取的全部SQE。

定义位置（Definition）：rtio.h:428。

符号定位：[rtio_sqe_drop_all](P001_RTIO公共接口.md#ga9486fb7b50e8d2409a50da235203536b)。

### `rtio_cqe_copy_out`

```c
int rtio_cqe_copy_out(struct rtio *r, struct rtio_cqe *cqes, size_t cqe_count, k_timeout_t timeout)
```

从队列中复制出CQE数组。

符号定位：[rtio_cqe_copy_out](P001_RTIO公共接口.md#ga98b2bbef95aea342a9b86a9775dd5c3b)。

### `rtio_flush_completion_queue`

```c
static int rtio_flush_completion_queue(struct rtio *r)
```

清空完成队列（Completion Queue）。

定义位置（Definition）：rtio.h:584。

符号定位：[rtio_flush_completion_queue](P001_RTIO公共接口.md#ga98b8f272b175ff2c0e9f5ed420c3abcc)。

### `rtio_access_revoke`

```c
static void rtio_access_revoke(struct rtio *r, struct k_thread *t)
```

撤销用户线程（User Thread）访问RTIO上下文的权限。

定义位置（Definition）：rtio.h:912。

符号定位：[rtio_access_revoke](P001_RTIO公共接口.md#ga9ab6490aa1893ae01bb0938a34c3e248)。

### `rtio_access_grant`

```c
static void rtio_access_grant(struct rtio *r, struct k_thread *t)
```

授予用户线程（User Thread）访问RTIO上下文的权限。

定义位置（Definition）：rtio.h:885。

符号定位：[rtio_access_grant](P001_RTIO公共接口.md#ga9da42c98546930575525f0f92710f9e4)。

### `rtio_cqe_release`

```c
static void rtio_cqe_release(struct rtio *r, struct rtio_cqe *cqe)
```

释放已取出的完成队列事件（CQE）。

定义位置（Definition）：rtio.h:570。

符号定位：[rtio_cqe_release](P001_RTIO公共接口.md#gaa0799a5f8ad98425d385a07c5d27d9cb)。

### `rtio_sqe_rx_buf`

```c
static int rtio_sqe_rx_buf(const struct rtio_iodev_sqe *iodev_sqe, uint32_t min_buf_len, uint32_t max_buf_len, uint8_t **buf, uint32_t *buf_len)
```

获取与接收提交（RX Submission）关联的缓冲区。

定义位置（Definition）：rtio.h:808。

符号定位：[rtio_sqe_rx_buf](P001_RTIO公共接口.md#gaab6843e2038d00a8354f57d7e2ffcf7e)。

### `rtio_set_cqe_callback`

```c
static int rtio_set_cqe_callback(struct rtio *r, rtio_cqe_callback_t callback, void *user_data)
```

设置完成队列事件回调（CQE Callback）。

定义位置（Definition）：rtio.h:475。

符号定位：[rtio_set_cqe_callback](P001_RTIO公共接口.md#gaabf5e6876e04f92f99a860591c7d310a)。

### `rtio_iodev_sqe_err`

```c
static void rtio_iodev_sqe_err(struct rtio_iodev_sqe *iodev_sqe, int result)
```

通知执行器（Executor）：一次提交已出错完成。

定义位置（Definition）：rtio.h:735。

符号定位：[rtio_iodev_sqe_err](P001_RTIO公共接口.md#gaada07aa6acefa548743b525225fa482f)。

### `rtio_sqe_cancel`

```c
int rtio_sqe_cancel(struct rtio_sqe *sqe)
```

尝试取消一个SQE。

符号定位：[rtio_sqe_cancel](P001_RTIO公共接口.md#gac01252e55d2848b38c0ed77b71d600a7)。

### `rtio_iodev_sqe_ok`

```c
static void rtio_iodev_sqe_ok(struct rtio_iodev_sqe *iodev_sqe, int result)
```

通知执行器（Executor）：一次提交已成功完成。

定义位置（Definition）：rtio.h:722。

符号定位：[rtio_iodev_sqe_ok](P001_RTIO公共接口.md#gacb1d2ffa2b07418d8a8aa319bd4336ab)。

### `rtio_cqe_acquire`

```c
static struct rtio_cqe * rtio_cqe_acquire(struct rtio *r)
```

如果可用，获取一个完成队列事件（CQE）。

定义位置（Definition）：rtio.h:443。

符号定位：[rtio_cqe_acquire](P001_RTIO公共接口.md#gad848646651fdf3649b882e5268f72a3c)。

### `rtio_cqe_consume`

```c
static struct rtio_cqe * rtio_cqe_consume(struct rtio *r)
```

如果可用，从完成队列中取出一个完成队列事件（CQE）。

定义位置（Definition）：rtio.h:512。

符号定位：[rtio_cqe_consume](P001_RTIO公共接口.md#gae562cf241911804cdb9f4e3a73b53df4)。

### `rtio_sqe_signal`

```c
void rtio_sqe_signal(struct rtio_sqe *sqe)
```

向一个等待操作SQE（AWAIT SQE）发送信号。

符号定位：[rtio_sqe_signal](P001_RTIO公共接口.md#gae63ffc626a3e99406d36aa47f10b49e1)。

### `rtio_iodev_sqe_next`

```c
static struct rtio_iodev_sqe * rtio_iodev_sqe_next(const struct rtio_iodev_sqe *iodev_sqe)
```

获取链或事务中的下一个SQE。

定义位置（Definition）：sqe.h:788。

符号定位：[rtio_iodev_sqe_next](P001_RTIO公共接口.md#gae690e3dc0fc40dda57257b2eed432719)。

### `rtio_cqe_get_mempool_buffer`

```c
int rtio_cqe_get_mempool_buffer(const struct rtio *r, struct rtio_cqe *cqe, uint8_t **buff, uint32_t *buff_len)
```

取得为该CQE分配的内存池缓冲区（Memory Pool Buffer）。

符号定位：[rtio_cqe_get_mempool_buffer](P001_RTIO公共接口.md#gaedbf9386a36ed99baa290ef6c318ded1)。

### `rtio_cqe_consume_block`

```c
static struct rtio_cqe * rtio_cqe_consume_block(struct rtio *r)
```

等待并从完成队列中取出一个完成队列事件（CQE）。

定义位置（Definition）：rtio.h:546。

符号定位：[rtio_cqe_consume_block](P001_RTIO公共接口.md#gaf617d05d9b59ce1f1d0697617ef6f249)。

### `rtio_sqe_acquire_array`

```c
static int rtio_sqe_acquire_array(struct rtio *r, size_t n, struct rtio_sqe **sqes)
```

如果可用，获取指定数量的提交队列事件（SQE）。

定义位置（Definition）：rtio.h:390。

符号定位：[rtio_sqe_acquire_array](P001_RTIO公共接口.md#gafb6e8c8679cb9483445c510cd6f14741)。

### `rtio_submit`

```c
int rtio_submit(struct rtio *r, uint32_t wait_count)
```

向底层执行器（Executor）提交I/O请求。

符号定位：[rtio_submit](P001_RTIO公共接口.md#gafee27c64a4a4989c4eb774addde8eb2e)。

### `k_sem_reset`

```c
void k_sem_reset(struct k_sem *sem)
```

将信号量计数重置为0。

符号定位：[k_sem_reset](../synchronization_reference/P008_信号量公共接口.md#ga1bd12d8d8c1b9c6be9b665d0fefe5562)。

### `k_sem_give`

```c
void k_sem_give(struct k_sem *sem)
```

释放信号量（Give a Semaphore）。

符号定位：[k_sem_give](../synchronization_reference/P008_信号量公共接口.md#gab9be3cf1988af2cd6afdace52d497c84)。

### `k_sem_take`

```c
int k_sem_take(struct k_sem *sem, k_timeout_t timeout)
```

获取信号量（Take a Semaphore）。

符号定位：[k_sem_take](../synchronization_reference/P008_信号量公共接口.md#gac71e2383c1920dddc45a561cacfef090)。

### `SYS_PORT_TRACING_FUNC_ENTER`

```c
#define SYS_PORT_TRACING_FUNC_ENTER(type, func,...)
```

用于记录可能返回值或不返回值的函数入口的跟踪宏（Tracing Macro）。

定义位置（Definition）：tracing_macros.h:246。

符号定位：[SYS_PORT_TRACING_FUNC_ENTER](../tracing_core_reference/P004_跟踪包装宏接口.md#ga445bcac4cec53d560ddca757de17e1e3)。

### `SYS_PORT_TRACING_FUNC_EXIT`

```c
#define SYS_PORT_TRACING_FUNC_EXIT(type, func,...)
```

用于记录函数执行结束的跟踪宏。

定义位置（Definition）：tracing_macros.h:272。

符号定位：[SYS_PORT_TRACING_FUNC_EXIT](../tracing_core_reference/P004_跟踪包装宏接口.md#gab0350eef3ed26733e57505ee2d0487cb)。

### `SYS_PORT_TRACING_FUNC`

```c
#define SYS_PORT_TRACING_FUNC(type, func,...)
```

用于记录不直接关联特定对象类型的函数调用的跟踪宏。

定义位置（Definition）：tracing_macros.h:233。

符号定位：[SYS_PORT_TRACING_FUNC](../tracing_core_reference/P004_跟踪包装宏接口.md#gadce691eea44f211b804ce44b51b2e71d)。

### `BIT`

```c
#define BIT(n)
```

将第n位设为1的无符号整数，在汇编语言中为有符号数。

定义位置（Definition）：util_macro.h:44。

符号定位：[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

### `CONTAINER_OF`

```c
#define CONTAINER_OF(ptr, type, field)
```

取得包含指定成员的结构体指针。

定义位置（Definition）：util.h:281。

符号定位：[CONTAINER_OF](../util_reference/P001_通用工具公共接口.md#gac5bc561d1bfd1bf68877fe577779bd2f)。

### `DIV_ROUND_UP`

```c
#define DIV_ROUND_UP(n, d)
```

执行除法并向上取整。

定义位置（Definition）：util.h:348。

符号定位：[DIV_ROUND_UP](../util_reference/P001_通用工具公共接口.md#gae664e7492e37d324831caf2321ddda37)。

### `EINVAL`

```c
#define EINVAL
```

参数无效（Invalid Argument）。

定义位置（Definition）：errno.h:61。

符号定位：[EINVAL](../error_reference/P003_系统错误号公共接口.md#ga2d1678d5a7cc8ce499643f3b8957def4)。

### `ENOMEM`

```c
#define ENOMEM
```

内存不足（Not Enough Core）。

定义位置（Definition）：errno.h:51。

符号定位：[ENOMEM](../error_reference/P003_系统错误号公共接口.md#ga6a05c923dad0c1208043e9c20a58c8e5)。

### `ENOTSUP`

```c
#define ENOTSUP
```

不支持的值（Unsupported Value）。

定义位置（Definition）：errno.h:115。

符号定位：[ENOTSUP](../error_reference/P003_系统错误号公共接口.md#ga91457bbf35f0f1085619a99423bb1f33)。

### `k_yield`

```c
void k_yield(void)
```

当前线程主动让出处理器（Yield）。

符号定位：[k_yield](../thread_core_reference/P001_线程公共接口.md#ga08a3484c33444ecedc2d71d78495a295)。

### `k_current_get`

```c
static __attribute_const__ k_tid_t k_current_get(void)
```

获取当前线程的线程标识（Thread ID）。

定义位置（Definition）：kernel.h:859。

符号定位：[k_current_get](../thread_core_reference/P001_线程公共接口.md#ga7ef1ed0fb9513df8096ede1e52fc76b2)。

### `k_object_access_grant`

```c
void k_object_access_grant(const void *object, struct k_thread *thread)
```

授予线程访问内核对象（Kernel Object）的权限。

符号定位：[k_object_access_grant](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#ga94087bedf96fe2a2bea437d3d585ca22)。

### `k_object_access_revoke`

```c
void k_object_access_revoke(const void *object, struct k_thread *thread)
```

撤销线程访问内核对象的权限。

符号定位：[k_object_access_revoke](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#gab70fe65497da1347cc4b7bf7ca2daf22)。

### `iodev.h`

RTIO输入输出设备（I/O Device）及相关函数。

符号定位：[iodev.h](../rtio_headers_reference/P005_RTIO设备头文件参考.md)。

### `kernel.h`

公共内核API（Public Kernel APIs）。

符号定位：[kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)。

### `mem_blocks.h`

内存块分配器（Memory Blocks Allocator）。

符号定位：[mem_blocks.h](../memblocks_reference/P002_内存块头文件参考.md)。

### `flags`

```c
flags
```

定义位置（Definition）：parser.h:86。

符号定位：[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

### `sqe.h`

RTIO提交队列事件（Submission Queue Events）及相关函数。

符号定位：[sqe.h](../rtio_headers_reference/P001_RTIO提交事件头文件参考.md)。

### `uint32_t`

```c
__UINT32_TYPE__ uint32_t
```

定义位置（Definition）：stdint.h:90。

符号定位：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

### `uint8_t`

```c
__UINT8_TYPE__ uint8_t
```

定义位置（Definition）：stdint.h:88。

符号定位：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

### `UINT16_MAX`

```c
#define UINT16_MAX
```

定义位置（Definition）：stdint.h:28。

符号定位：[UINT16_MAX](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3ea490c9b3617d4479bd80ef93cd5602)。

### `uintptr_t`

```c
__UINTPTR_TYPE__ uintptr_t
```

定义位置（Definition）：stdint.h:105。

符号定位：[uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)。

### `uint16_t`

```c
__UINT16_TYPE__ uint16_t
```

定义位置（Definition）：stdint.h:89。

符号定位：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

### `string.h`

符号定位：[string.h](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html)。

### `memset`

```c
void * memset(void *buf, int c, size_t n)
```

符号定位：[memset](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#a4137694174d4ca2fad886a1db355015c)。

### `k_mem_partition`

内存分区（Memory Partition）。

定义位置（Definition）：mem_domain.h:55。

符号定位：[k_mem_partition](../memory_domain_reference/P005_内存分区结构.md)。

### `k_sem`

信号量结构体（Semaphore Structure）。

定义位置（Definition）：kernel.h:3738。

符号定位：[k_sem](../synchronization_reference/P009_内核信号量结构.md)。

### `k_thread`

线程结构体（Thread Structure）。

定义位置（Definition）：thread.h:258。

符号定位：[k_thread](../thread_core_reference/P004_线程对象结构.md)。

### `k_timeout_t`

内核超时类型（Kernel Timeout Type）。

定义位置（Definition）：clock.h:65。

符号定位：[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

### `k_timepoint_t`

内核时间点类型（Kernel Timepoint Type）。

定义位置（Definition）：clock.h:289。

符号定位：[k_timepoint_t](../timer_reference/P088_内核时间点类型.md)。

### `mpsc_node`

队列成员（Queue Member）。

定义位置（Definition）：mpsc_lockfree.h:79。

符号定位：[mpsc_node](../intercore_reference/P160_MPSC无锁队列节点.md)。

### `mpsc`

多生产者单消费者队列（Multi-Producer Single-Consumer Queue，MPSC Queue）。

定义位置（Definition）：mpsc_lockfree.h:86。

符号定位：[mpsc](../intercore_reference/P159_MPSC无锁队列结构.md)。

### `rtio_cqe`

一个完成队列事件（Completion Queue Event）。

定义位置（Definition）：cqe.h:90。

符号定位：[rtio_cqe](../rtio_model_reference/P002_RTIO完成事件.md)。

### `rtio_cqe::userdata`

```c
void * userdata
```

与操作关联的用户数据。

定义位置（Definition）：cqe.h:96。

符号定位：[rtio_cqe::userdata](../rtio_model_reference/P002_RTIO完成事件.md#a15128387ccbea55812ef229eab7241e7)。

### `rtio_cqe::flags`

```c
uint32_t flags
```

与操作关联的标志。

定义位置（Definition）：cqe.h:97。

符号定位：[rtio_cqe::flags](../rtio_model_reference/P002_RTIO完成事件.md#a8a7632ef1cfd31529d782bd761908d93)。

### `rtio_cqe::result`

```c
int32_t result
```

操作的结果。

定义位置（Definition）：cqe.h:95。

符号定位：[rtio_cqe::result](../rtio_model_reference/P002_RTIO完成事件.md#acbe2e6607a752b676d9336b9ca6ce435)。

### `rtio_iodev_sqe`

输入输出设备提交队列条目（I/O Device Submission Queue Entry）。

定义位置（Definition）：sqe.h:403。

符号定位：[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)。

### `rtio_iodev_sqe::sqe`

```c
struct rtio_sqe sqe
```

此条目携带的提交。

定义位置（Definition）：sqe.h:404。

符号定位：[rtio_iodev_sqe::sqe](../rtio_model_reference/P005_RTIO设备提交条目.md#a2bd98599678909c0ddb22f879affa12b)。

### `rtio_iodev_sqe::r`

```c
struct rtio * r
```

该提交所属的RTIO上下文。

定义位置（Definition）：sqe.h:407。

符号定位：[rtio_iodev_sqe::r](../rtio_model_reference/P005_RTIO设备提交条目.md#a3c3a050793589258eab5ff5ac30f24c8)。

### `rtio_iodev_sqe::q`

```c
struct mpsc_node q
```

用于将此条目入队的链接。

定义位置（Definition）：sqe.h:405。

符号定位：[rtio_iodev_sqe::q](../rtio_model_reference/P005_RTIO设备提交条目.md#a9cfdd004b65a5e2bc111bc2fb333498c)。

### `rtio_pool`

供动态创建的线程使用的RTIO上下文池（Context Pool）。

定义位置（Definition）：rtio.h:1132。

符号定位：[rtio_pool](../rtio_model_reference/P006_RTIO上下文池.md)。

### `rtio_pool::contexts`

```c
struct rtio ** contexts
```

包含池内各上下文的数组。

定义位置（Definition）：rtio.h:1137。

符号定位：[rtio_pool::contexts](../rtio_model_reference/P006_RTIO上下文池.md#a5a148773dcd269e1d29be95c77fb6d99)。

### `rtio_pool::used`

```c
atomic_t * used
```

用于指示成员已使用或未使用的原子位图（Atomic Bitmap）。

定义位置（Definition）：rtio.h:1140。

符号定位：[rtio_pool::used](../rtio_model_reference/P006_RTIO上下文池.md#a89240a8b8e9809d3f61ef903d24e3db2)。

### `rtio_pool::pool_size`

```c
size_t pool_size
```

池的大小。

定义位置（Definition）：rtio.h:1134。

符号定位：[rtio_pool::pool_size](../rtio_model_reference/P006_RTIO上下文池.md#abe49ac5f1cec586855dc5318e3091419)。

### `rtio_sqe`

一个提交队列事件（Submission Queue Event）。

定义位置（Definition）：sqe.h:310。

符号定位：[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)。

### `rtio_sqe::userdata`

```c
void * userdata
```

用户提供的数据，在操作完成时返回。

定义位置（Definition）：sqe.h:328。

符号定位：[rtio_sqe::userdata](../rtio_model_reference/P007_RTIO提交事件.md#a0ed519ee0b5867ff73bdaf37f983c971)。

### `rtio_sqe::op`

```c
uint8_t op
```

操作码（Operation Code）。

定义位置（Definition）：sqe.h:311。

符号定位：[rtio_sqe::op](../rtio_model_reference/P007_RTIO提交事件.md#a1d8d3e3426e47a2c7f54d98f51acd953)。

### `rtio_sqe::rx`

```c
struct rtio_sqe::@126267262255374054123217063150244034155174062054::@222067021034074304061254367152327164076222165070 rx
```

`OP_RX`接收操作。

符号定位：[rtio_sqe::rx](../rtio_model_reference/P007_RTIO提交事件.md#a29e0c1b06b6f7b604af147a231b46319)。

### `rtio_sqe::await`

```c
struct rtio_sqe::@126267262255374054123217063150244034155174062054::@236333123355174166163204241333175337261032350217 await
```

`OP_AWAIT`等待操作。

符号定位：[rtio_sqe::await](../rtio_model_reference/P007_RTIO提交事件.md#a64f5db04d58882832f86477628c25be3)。

### `rtio_sqe::buf_len`

```c
uint32_t buf_len
```

缓冲区长度。

定义位置（Definition）：sqe.h:335。

符号定位：[rtio_sqe::buf_len](../rtio_model_reference/P007_RTIO提交事件.md#a67376f40a13960b152a23da250275722)。

### `rtio_sqe::flags`

```c
uint16_t flags
```

操作标志（Operation Flags）。

定义位置（Definition）：sqe.h:315。

符号定位：[rtio_sqe::flags](../rtio_model_reference/P007_RTIO提交事件.md#aad2ff8524df0e24b812e77e2393bf5b0)。

### `rtio_sqe::buf`

```c
const uint8_t * buf
```

写操作的数据来源缓冲区。

定义位置（Definition）：sqe.h:336。

符号定位：[rtio_sqe::buf](../rtio_model_reference/P007_RTIO提交事件.md#ab71176c084e8b8eb65dfeb3018ae2a49)。

### `rtio_sqe::callback`

```c
rtio_callback_t callback
```

要运行的函数。

定义位置（Definition）：sqe.h:353。

符号定位：[rtio_sqe::callback](../rtio_model_reference/P007_RTIO提交事件.md#af8c31c33e9fedebe55cac73595d0f696)。

### `rtio`

一个RTIO上下文（Context），其内容可以视为一对队列。

定义位置（Definition）：rtio.h:83。

符号定位：[rtio](../rtio_model_reference/P001_RTIO上下文.md)。

### `rtio::cqe_pool`

```c
struct rtio_cqe_pool * cqe_pool
```

带空闲链表（Free List）的完成队列对象池。

定义位置（Definition）：rtio.h:111。

符号定位：[rtio::cqe_pool](../rtio_model_reference/P001_RTIO上下文.md#a1bce3c3bb0150275ece65975adf3ee4f)。

### `rtio::sq`

```c
struct mpsc sq
```

提交队列（Submission Queue）。

定义位置（Definition）：rtio.h:119。

符号定位：[rtio::sq](../rtio_model_reference/P001_RTIO上下文.md#a34fbabfdbef3144f4520bf678684cdfb)。

### `rtio::cq_count`

```c
atomic_t cq_count
```

完成事件总数。

定义位置（Definition）：rtio.h:102。

符号定位：[rtio::cq_count](../rtio_model_reference/P001_RTIO上下文.md#a358de1033ab4396d1f1baee2699c993f)。

### `rtio::sqe_pool`

```c
struct rtio_sqe_pool * sqe_pool
```

带空闲链表（Free List）的提交队列对象池。

定义位置（Definition）：rtio.h:108。

符号定位：[rtio::sqe_pool](../rtio_model_reference/P001_RTIO上下文.md#a955f012bac623e7c037b5f1dba8e7fda)。

### `rtio::xcqcnt`

```c
atomic_t xcqcnt
```

因没有可用CQE而丢弃的完成事件数量。

定义位置（Definition）：rtio.h:105。

符号定位：[rtio::xcqcnt](../rtio_model_reference/P001_RTIO上下文.md#ac45facdcc6d64cd70113b9b05b2fb086)。

### `rtio::cq`

```c
struct mpsc cq
```

完成队列（Completion Queue）。

定义位置（Definition）：rtio.h:122。

符号定位：[rtio::cq](../rtio_model_reference/P001_RTIO上下文.md#ad6f44a354a170cb04a584beee7728fa9)。

### `iterable_sections.h`

可迭代段（Iterable Sections）辅助工具。

符号定位：[iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)。

### `util.h`

杂项工具（Miscellaneous Utilities）。

符号定位：[util.h](../util_reference/P002_通用工具头文件参考.md)。

### `k_is_user_context`

```c
static bool k_is_user_context(void)
```

指示CPU当前是否处于用户模式（User Mode）。

定义位置（Definition）：syscall.h:120。

符号定位：[k_is_user_context](../syscall_boot_reference/P002_系统调用头文件参考.md#abc92c4d00c42f08c7600602c8847f021)。

## 3.4\_源码跟踪译注

> 译注——上下文（Context）把提交队列、完成队列和各自的对象池组织在一起。`rtio_sqe_acquire()`成功后已把条目放入待提交队列，调用者仍需填写操作；`rtio_submit()`才启动执行。`rtio_sqe_acquirable()`只是当前可用量，不能据此推导出并发调用间的预留保证。`rtio_sqe_acquire_array()`失败会归还已经取得的条目，但输出数组按原文约定不可使用；`rtio_sqe_drop_all()`清理的是该上下文整个待提交队列。

> 译注——完成事件对象（CQE）与有效载荷缓冲区（Payload Buffer）是两种资源。消费CQE后用`rtio_cqe_release(r, cqe)`归还事件槽；通过内存池读操作取得的数据缓冲区，应先获取并处理，再用`rtio_release_buffer()`归还。`rtio_flush_completion_queue()`只取出当下可消费的CQE、释放事件槽并保留遇到的首个负结果，不等待所有在途操作，也不替代数据缓冲区的归还。

> 译注——等待完成（Wait for Completion）不等于读取结果。`rtio_submit(r, wait_count)`等待完成计数达到要求；每次`rtio_cqe_submit()`即使没有空闲CQE、仅增加丢弃计数`xcqcnt`，仍会推进`cq_count`与提交等待计数。因此成功返回不能证明已经取到全部结果或所有I/O成功。`RTIO_SQE_NO_RESPONSE`、提交前取消等不产生完成事件的路径不能计入预期CQE数量，否则等待可能无法结束。

> 译注——回调在产生完成事件的调用路径上直接执行，没有自动切换到工作线程。`rtio_set_cqe_callback()`仅在`CONFIG_RTIO_CQE_CALLBACK`启用时可用，修改时必须满足原文要求：没有SQE正在执行。`rtio_cqe_produce()`本身只将事件入队；信号量通知、回调和完成计数由`rtio_cqe_submit()`处理。不能把两者当成等价替换。

> 译注——取消（Cancellation）是标志请求，不是中止硬件的保证。`z_impl_rtio_sqe_cancel()`沿已有链接设置`RTIO_SQE_CANCELED`；执行器会在适当阶段检查。提交前已取消的条目会附加`RTIO_SQE_NO_RESPONSE`，单次完成处理也可能不生成CQE，因此原文“产生-ECANCELED失败”不能理解成每次取消必定收到一个失败CQE。句柄只在对应SQE仍有效时使用，不能在对象回收复用后继续取消。

> 译注——链（Chain）与事务（Transaction）的失败描述按原文保留。当前读取的`rtio_executor_handle_oneshot()`在错误路径上把事务内后续结果设为`-ECANCELED`，但循环后的CHAINED分支仍调用`rtio_iodev_submit(curr, last_result)`，没有在此处统一为后续链设置取消标志。仅凭本次源码不能把原文“所有链接操作都会失败”当作已验证的全链行为；实际依赖该约定时需要对照所使用版本及驱动补充验证。本次没有修改实现。

> 译注——内存池读操作（Mempool Read）通过CQE标志记录块索引和数量；数据缓冲区的实际容量可能按块大小向上取整。释放说明声称长度会向上取整，但本次`rtio_block_pool_free()`实际以右移计算块数。应传回取得时的完整缓冲区指针和实际分配长度，不能以有效数据字节数代替，也不要把“忽略无效参数”理解成任意错误地址与长度都能被安全接受。

> 译注——多次完成读操作（Multishot Read）正常完成后会重新排队，并为下次内存池读清空原缓冲区字段以便重新分配；读取的执行器在取消或错误路径上停止重提并释放资源。原文的“持续到取消”不是错误后仍自动重试的保证。应用仍需按各完成事件的结果和所有权处理数据。

> 译注——用户空间（Userspace）权限授予涉及上下文、按配置存在的信号量及共享延时IODEV，不代表任意外设IODEV也自动授权。系统调用校验会检查操作码、对象权限和读写缓冲区；不能把内核可准备的所有操作都推定为用户模式可用。上下文池释放仅处理权限和占用位，不会自动排空SQE、CQE或释放全部在途数据；归还前应完成所属工作并清理资源。

> 译注——源码定位均为相对路径。本页链接的本仓库文件用于追踪同名实现，是否与滚动更新的官方main一致应另行比较；本次结论以来源记录中的官方文件SHA-256为界。

> 译注——原文写作`rtio_cq_release(r)`，本次公开声明与实现中的释放入口为`rtio_cqe_release(r, cqe)`；正文保留旧名称以便核对原文，实际代码应按当前声明传入上下文和CQE。

> 译注——原文写作`rtio_cq_release(r)`，当前入口为`rtio_cqe_release(r, cqe)`。阻塞消费没有超时参数，不代表所有已经提交的操作都已结束。

> 译注——原文参数说明误写为SQE数组及数量，函数声明实际是`struct rtio_cqe *cqes`和`cqe_count`。原文还将总超时描述为`timeout*cqe_count`，但本次实现只在循环前计算一次`end = sys_timepoint_calc(timeout)`，不会逐个事件重置截止点；K_FOREVER分支使用阻塞消费。实现采用do-while，也没有在入口对0数量提前返回，调用者应提供正数容量。

> 译注——原文的`rtio_sqe_read_with_pool()`是旧名称，本次公开辅助函数为`rtio_sqe_prep_read_with_pool()`。成功获取缓冲区信息不释放CQE或缓冲区；块数为0时实现返回NULL缓冲区及0长度。

> 译注——原文的`rtio_sqe_read_with_pool()`对应当前`rtio_sqe_prep_read_with_pool()`。本次释放入口只先排除空上下文、空指针、空块池或0长度，再调用块池释放；长度在内部按右移计算块数，与原文“向上取整”不一致，实际应保留并传回分配长度。

> 译注——原文参数说明中的CEQ为原拼写，此处对应CQE标志。CQE对象不足时丢弃事件并增加xcqcnt，但完成计数仍递增；不能把submit等待结束等同于结果已保存到完成队列。

> 译注——尽管名称使用handles复数，输出参数只保存第一个生成的SQE句柄；实现复制SQE结构体，不深复制其指针指向的数据缓冲区。空间预检不提供跨并发调用的资源预留。

> 译注——本次Doxygen页面展示的是禁用CONFIG_RTIO_OP_DELAY时触发BUILD_ASSERT的宏分支；启用时同名入口是静态内联函数。原文称设置内核定时器（Kernel Timer）。本次sqe.h把操作交给共享rtio_timeout_iodev，rtio_timeout.c实际使用单个内核_timeout和按到期时间排序的列表，没有为每个SQE创建k_timer。延时从IODEV提交时计算，不从准备SQE时计算。

> 译注——本次准备函数将await.ok初始化为0；等待注册回调后以CAS将其变为1，发送信号也执行0→1的CAS，后到的一方在CAS失败后调用回调。这是单次等待与信号的交会机制，不是任意次数信号的计数器；重复发信号与已回收SQE不在安全使用前提内。

> 译注——本次宏优先考虑DTCM和NOCACHE内存放置配置，只有默认分支才按CONFIG_USERSPACE选择K_APP_BMEM或普通static。原文描述保留，但不能把它视为所有配置下的完整展开。

> 译注——本次宏优先考虑DTCM和NOCACHE内存放置配置，默认分支才按CONFIG_USERSPACE选择K_APP_DMEM或普通static。

头文件相对定位：[include/zephyr/rtio/rtio.h](../../../include/zephyr/rtio/rtio.h)，关联实现／接口：[subsys/rtio/rtio_executor.c](../../../subsys/rtio/rtio_executor.c)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/rtio/rtio.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/rtio/rtio_executor.c)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 3.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P002_RTIO核心头文件参考.md)
- [string.h](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html)
- [zephyr/app_memory/app_memdomain.h](../memory_domain_reference/P009_应用内存域头文件参考.md)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/sys/atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [zephyr/sys/mem_blocks.h](../memblocks_reference/P002_内存块头文件参考.md)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [zephyr/rtio/sqe.h](../rtio_headers_reference/P001_RTIO提交事件头文件参考.md)
- [zephyr/rtio/cqe.h](../rtio_headers_reference/P003_RTIO完成事件头文件参考.md)
- [zephyr/rtio/iodev.h](../rtio_headers_reference/P005_RTIO设备头文件参考.md)
- [rtio](../rtio_model_reference/P001_RTIO上下文.md)
- [rtio_cqe_callback_t](P001_RTIO公共接口.md#ga6adaa4d7ef1fa8054000d8d9b8e634bd)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [cq_count](../rtio_model_reference/P001_RTIO上下文.md#a358de1033ab4396d1f1baee2699c993f)
- [xcqcnt](../rtio_model_reference/P001_RTIO上下文.md#ac45facdcc6d64cd70113b9b05b2fb086)
- [sqe_pool](../rtio_model_reference/P001_RTIO上下文.md#a955f012bac623e7c037b5f1dba8e7fda)
- [cqe_pool](../rtio_model_reference/P001_RTIO上下文.md#a1bce3c3bb0150275ece65975adf3ee4f)
- [mpsc](../intercore_reference/P159_MPSC无锁队列结构.md)
- [sq](../rtio_model_reference/P001_RTIO上下文.md#a34fbabfdbef3144f4520bf678684cdfb)
- [cq](../rtio_model_reference/P001_RTIO上下文.md#ad6f44a354a170cb04a584beee7728fa9)
- [rtio_mempool_block_size](P001_RTIO公共接口.md#ga4213be028b0a1264daaa0d30c4c2d089)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)
- [UINT16_MAX](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3ea490c9b3617d4479bd80ef93cd5602)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [ENOTSUP](../error_reference/P003_系统错误号公共接口.md#ga91457bbf35f0f1085619a99423bb1f33)
- [ENOMEM](../error_reference/P003_系统错误号公共接口.md#ga6a05c923dad0c1208043e9c20a58c8e5)
- [DIV_ROUND_UP](../util_reference/P001_通用工具公共接口.md#gae664e7492e37d324831caf2321ddda37)
- [sys_mem_blocks_alloc_contiguous](../memblocks_reference/P001_内存块分配公共接口.md#ga72614d0c120f40209837b77d0333bb23)
- [sys_mem_blocks_free_contiguous](../memblocks_reference/P001_内存块分配公共接口.md#ga39e7f8dfe3bda8eabc2372f9a1e87342)
- [k_mem_partition](../memory_domain_reference/P005_内存分区结构.md)
- [rtio_partition](P001_RTIO公共接口.md#ga86a38086dd85150ab6e479d73db1c6d1)
- [rtio_sqe_acquirable](P001_RTIO公共接口.md#ga1f4fb7bccbaae08a94387e4b11275a78)
- [rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)
- [rtio_sqe_acquire](P001_RTIO公共接口.md#ga8b47c954d15a334621def53acceb6799)
- [SYS_PORT_TRACING_FUNC_ENTER](../tracing_core_reference/P004_跟踪包装宏接口.md#ga445bcac4cec53d560ddca757de17e1e3)
- [rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)
- [r](../rtio_model_reference/P005_RTIO设备提交条目.md#a3c3a050793589258eab5ff5ac30f24c8)
- [SYS_PORT_TRACING_FUNC_EXIT](../tracing_core_reference/P004_跟踪包装宏接口.md#gab0350eef3ed26733e57505ee2d0487cb)
- [mpsc_push](../intercore_reference/P158_MPSC无锁队列接口.md#ga403add133841ef88e10d74141e782b37)
- [q](../rtio_model_reference/P005_RTIO设备提交条目.md#a9cfdd004b65a5e2bc111bc2fb333498c)
- [sqe](../rtio_model_reference/P005_RTIO设备提交条目.md#a2bd98599678909c0ddb22f879affa12b)
- [rtio_sqe_acquire_array](P001_RTIO公共接口.md#gafb6e8c8679cb9483445c510cd6f14741)
- [CONTAINER_OF](../util_reference/P001_通用工具公共接口.md#gac5bc561d1bfd1bf68877fe577779bd2f)
- [rtio_sqe_drop_all](P001_RTIO公共接口.md#ga9486fb7b50e8d2409a50da235203536b)
- [mpsc_node](../intercore_reference/P160_MPSC无锁队列节点.md)
- [mpsc_pop](../intercore_reference/P158_MPSC无锁队列接口.md#ga823ec37b84ac43e46167aac954bce9d7)
- [rtio_cqe](../rtio_model_reference/P002_RTIO完成事件.md)
- [rtio_cqe_acquire](P001_RTIO公共接口.md#gad848646651fdf3649b882e5268f72a3c)
- [memset](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#a4137694174d4ca2fad886a1db355015c)
- [rtio_set_cqe_callback](P001_RTIO公共接口.md#gaabf5e6876e04f92f99a860591c7d310a)
- [rtio_cqe_produce](P001_RTIO公共接口.md#ga6f55202adeca60aed0343a7a0dcab071)
- [rtio_cqe_consume](P001_RTIO公共接口.md#gae562cf241911804cdb9f4e3a73b53df4)
- [k_sem_take](../synchronization_reference/P008_信号量公共接口.md#gac71e2383c1920dddc45a561cacfef090)
- [K_NO_WAIT](../timer_reference/P086_系统时钟公共接口.md#ga3d9541cfe2e8395af66d186efa77362f)
- [rtio_cqe_consume_block](P001_RTIO公共接口.md#gaf617d05d9b59ce1f1d0697617ef6f249)
- [K_FOREVER](../timer_reference/P086_系统时钟公共接口.md#ga0bb4b83f0222193b21a8910311bab0ca)
- [rtio_cqe_release](P001_RTIO公共接口.md#gaa0799a5f8ad98425d385a07c5d27d9cb)
- [SYS_PORT_TRACING_FUNC](../tracing_core_reference/P004_跟踪包装宏接口.md#gadce691eea44f211b804ce44b51b2e71d)
- [rtio_flush_completion_queue](P001_RTIO公共接口.md#ga98b8f272b175ff2c0e9f5ed420c3abcc)
- [result](../rtio_model_reference/P002_RTIO完成事件.md#acbe2e6607a752b676d9336b9ca6ce435)
- [rtio_sqe_signal](P001_RTIO公共接口.md#gae63ffc626a3e99406d36aa47f10b49e1)
- [atomic_cas](../atomic_reference/P001_原子操作公共接口.md#gab879da5aa1ffcc317adc664c016586f7)
- [await](../rtio_model_reference/P007_RTIO提交事件.md#a64f5db04d58882832f86477628c25be3)
- [callback](../rtio_model_reference/P007_RTIO提交事件.md#af8c31c33e9fedebe55cac73595d0f696)
- [userdata](../rtio_model_reference/P007_RTIO提交事件.md#a0ed519ee0b5867ff73bdaf37f983c971)
- [rtio_cqe_compute_flags](P001_RTIO公共接口.md#ga75661c8c6c94a0ac6254cec674b478c8)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [op](../rtio_model_reference/P007_RTIO提交事件.md#a1d8d3e3426e47a2c7f54d98f51acd953)
- [RTIO_OP_RX](../rtio_model_reference/P009_RTIO操作码.md#gafeb05c351207cd1638fa78f6607e1a4a)
- [flags](../rtio_model_reference/P007_RTIO提交事件.md#aad2ff8524df0e24b812e77e2393bf5b0)
- [RTIO_SQE_MEMPOOL_BUFFER](../rtio_model_reference/P010_RTIO提交事件标志.md#ga2802b46584220afffa0e959e149d5a4d)
- [rx](../rtio_model_reference/P007_RTIO提交事件.md#a29e0c1b06b6f7b604af147a231b46319)
- [buf](../rtio_model_reference/P007_RTIO提交事件.md#ab71176c084e8b8eb65dfeb3018ae2a49)
- [buf_len](../rtio_model_reference/P007_RTIO提交事件.md#a67376f40a13960b152a23da250275722)
- [RTIO_CQE_FLAG_PREP_MEMPOOL](../rtio_model_reference/P008_RTIO完成事件标志.md#ga28b3a5661248b6b3763aab47417114d6)
- [rtio_cqe_get_mempool_buffer](P001_RTIO公共接口.md#gaedbf9386a36ed99baa290ef6c318ded1)
- [RTIO_CQE_FLAG_GET](../rtio_model_reference/P008_RTIO完成事件标志.md#gaef64ea020a20ac22a0edcb6eca032efc)
- [flags](../rtio_model_reference/P002_RTIO完成事件.md#a8a7632ef1cfd31529d782bd761908d93)
- [RTIO_CQE_FLAG_MEMPOOL_BUFFER](../rtio_model_reference/P008_RTIO完成事件标志.md#ga0f212500447a5e37e225a6997953b609)
- [RTIO_CQE_FLAG_MEMPOOL_GET_BLK_IDX](../rtio_model_reference/P008_RTIO完成事件标志.md#ga0b5f3f7e7be472ecf87bd2b08c1888da)
- [RTIO_CQE_FLAG_MEMPOOL_GET_BLK_CNT](../rtio_model_reference/P008_RTIO完成事件标志.md#ga087465f866d417d5332602bb582cc1a7)
- [EINVAL](../error_reference/P003_系统错误号公共接口.md#ga2d1678d5a7cc8ce499643f3b8957def4)
- [rtio_iodev_sqe_ok](P001_RTIO公共接口.md#gacb1d2ffa2b07418d8a8aa319bd4336ab)
- [rtio_iodev_sqe_err](P001_RTIO公共接口.md#gaada07aa6acefa548743b525225fa482f)
- [rtio_cqe_submit](P001_RTIO公共接口.md#ga4abc221d5a90ab882000a72caa0ebd0f)
- [atomic_inc](../atomic_reference/P001_原子操作公共接口.md#gaae47a9cbe5a6534967b417f602b37ac2)
- [userdata](../rtio_model_reference/P002_RTIO完成事件.md#a15128387ccbea55812ef229eab7241e7)
- [k_sem_give](../synchronization_reference/P008_信号量公共接口.md#gab9be3cf1988af2cd6afdace52d497c84)
- [atomic_get](../atomic_reference/P001_原子操作公共接口.md#ga33bb426a17535bd1022895a7e44b32fa)
- [rtio_sqe_rx_buf](P001_RTIO公共接口.md#gaab6843e2038d00a8354f57d7e2ffcf7e)
- [rtio_release_buffer](P001_RTIO公共接口.md#ga6530bf56ccbab046a362a6448f941609)
- [rtio_access_grant](P001_RTIO公共接口.md#ga9da42c98546930575525f0f92710f9e4)
- [k_thread](../thread_core_reference/P004_线程对象结构.md)
- [k_object_access_grant](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#ga94087bedf96fe2a2bea437d3d585ca22)
- [rtio_access_revoke](P001_RTIO公共接口.md#ga9ab6490aa1893ae01bb0938a34c3e248)
- [k_object_access_revoke](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#gab70fe65497da1347cc4b7bf7ca2daf22)
- [rtio_sqe_cancel](P001_RTIO公共接口.md#gac01252e55d2848b38c0ed77b71d600a7)
- [RTIO_SQE_CANCELED](../rtio_model_reference/P010_RTIO提交事件标志.md#ga7f7f9b038ab8409f271b1aebc1b95ee6)
- [rtio_iodev_sqe_next](P001_RTIO公共接口.md#gae690e3dc0fc40dda57257b2eed432719)
- [rtio_sqe_copy_in_get_handles](P001_RTIO公共接口.md#ga830863e6c8d9b96f4c473a038cab8f8c)
- [rtio_sqe_copy_in](P001_RTIO公共接口.md#ga65e351af0a16dcf504a51ef4eb9316c7)
- [rtio_cqe_copy_out](P001_RTIO公共接口.md#ga98b2bbef95aea342a9b86a9775dd5c3b)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [k_timepoint_t](../timer_reference/P088_内核时间点类型.md)
- [sys_timepoint_calc](../timer_reference/P086_系统时钟公共接口.md#ga509cf4599c1f162c97540743e8c21d33)
- [K_TIMEOUT_EQ](../timer_reference/P086_系统时钟公共接口.md#ga9abf00b34e16ab7ad0883603b6778b1b)
- [sys_timepoint_expired](../timer_reference/P086_系统时钟公共接口.md#ga87d0d7a0f7bcdcc8c4909962eac12985)
- [rtio_submit](P001_RTIO公共接口.md#gafee27c64a4a4989c4eb774addde8eb2e)
- [k_is_in_isr](../fatal_irq_reference/P007_中断服务接口.md#ga8482b0dd2283d12677a9ebe321667d16)
- [k_sem_reset](../synchronization_reference/P008_信号量公共接口.md#ga1bd12d8d8c1b9c6be9b665d0fefe5562)
- [k_yield](../thread_core_reference/P001_线程公共接口.md#ga08a3484c33444ecedc2d71d78495a295)
- [rtio_pool](../rtio_model_reference/P006_RTIO上下文池.md)
- [pool_size](../rtio_model_reference/P006_RTIO上下文池.md#abe49ac5f1cec586855dc5318e3091419)
- [contexts](../rtio_model_reference/P006_RTIO上下文池.md#a5a148773dcd269e1d29be95c77fb6d99)
- [used](../rtio_model_reference/P006_RTIO上下文池.md#a89240a8b8e9809d3f61ef903d24e3db2)
- [rtio_pool_acquire](P001_RTIO公共接口.md#ga37c94f84cfce3810fd598040aba3841e)
- [atomic_test_and_set_bit](../atomic_reference/P001_原子操作公共接口.md#ga7ff45e13aa5f8be5d7a550e49f5c720b)
- [k_current_get](../thread_core_reference/P001_线程公共接口.md#ga7ef1ed0fb9513df8096ede1e52fc76b2)
- [rtio_pool_release](P001_RTIO公共接口.md#ga05e24d59485f71cc0126d44abbe8cf2b)
- [k_is_user_context](../syscall_boot_reference/P002_系统调用头文件参考.md#abc92c4d00c42f08c7600602c8847f021)
- [atomic_clear_bit](../atomic_reference/P001_原子操作公共接口.md#ga1c1693d524c49d11fd32b323a39d718e)

---

[上一章](P002_RTIO核心头文件参考.md) · [返回大纲](大纲.md)

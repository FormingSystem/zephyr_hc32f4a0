/*
 * SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors
 * SPDX-License-Identifier: Apache-2.0
 */
#include <errno.h>
#include <stdint.h>
#include <zephyr/sys/printk.h>
#include <zephyr/ztest.h>

/** @brief 累加最多四个采样值；失败时不改变调用者的输出。 */
static int sample_sum(const uint16_t *values, size_t count, uint32_t *result)
{
	uint32_t total = 0;

	if (values == NULL || result == NULL || count == 0 || count > 4) {
		return -EINVAL;
	}
	for (size_t i = 0; i < count; ++i) {
		total += values[i];
	}
	*result = total;
	return 0;
}

/** @brief 正常计算，并用错误预期验证断言失败能传播到主机。 */
ZTEST(first_evidence, test_sum)
{
	const uint16_t input[] = {10, 20, 30};
	uint32_t result = 0;
	int rc = sample_sum(input, ARRAY_SIZE(input), &result);
	uint32_t expected = IS_ENABLED(CONFIG_LEARNING_INJECT_FAILURE) ? 61 : 60;

	printk("sample count=%u rc=%d sum=%u expected=%u\n",
	       (unsigned int)ARRAY_SIZE(input), rc, (unsigned int)result,
	       (unsigned int)expected);
	zassert_equal(rc, 0, "valid input must succeed");
	zassert_equal(result, expected, "sample sum differs from expectation");
}

/** @brief 无效输入必须在读取数组前被拒绝，输出保持原值。 */
ZTEST(first_evidence, test_reject_empty)
{
	const uint16_t input[] = {10};
	uint32_t result = 1234;

	zassert_equal(sample_sum(input, 0, &result), -EINVAL, "empty input must fail");
	zassert_equal(result, 1234, "failure must preserve the output");
}

ZTEST_SUITE(first_evidence, NULL, NULL, NULL, NULL, NULL);

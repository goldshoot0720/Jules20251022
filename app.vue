<template>
  <div>
    <UHeader>
      <template #logo>
        Jules20251022
      </template>
      <template #right>
        <UButton to="/food" color="white" variant="ghost">食物管理</UButton>
        <UButton to="/subscription" color="white" variant="ghost">訂閱管理</UButton>
        <UButton to="/winning" color="white" variant="ghost">中獎頁面</UButton>
        <UButton to="/personal-introduction" color="white" variant="ghost">個人簡介</UButton>
      </template>
    </UHeader>
    <NuxtPage />
    <UNotifications />
  </div>
</template>

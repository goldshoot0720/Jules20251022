<template>
  <div>
    <UHeader>
      <template #logo>
        Jules20251022
      </template>
      <template #right>
        <UButton to="/food" color="white" variant="ghost">Food</UButton>
        <UButton to="/subscription" color="white" variant="ghost">Subscription</UButton>
      </template>
    </UHeader>
    <NuxtPage />
    <UNotifications />
  </div>
</template>

interface Policies {
    uppercase: boolean;
    lowercase: boolean;
    numeric: boolean;
    special: boolean;
  }
  
  interface PasswordSettings {
    minLength: number;
    maxAttempts: number;
    availabilityTime: number;
  }
  
  export const validatePassword = (password: string, policies: Policies, minLength: number): boolean => {
    const isValid = Object.entries(policies).every(([key, enabled]) => {
      if (!enabled) return true;
      if (key === 'uppercase') return /[A-Z]/.test(password);
      if (key === 'lowercase') return /[a-z]/.test(password);
      if (key === 'numeric') return /[0-9]/.test(password);
      if (key === 'special') return /[!@#$%^&*()_+{}\[\]:;"'<>,.?/~`-]/.test(password);
      return true;
    }) && password.length >= minLength;
  
    return isValid;
  };
  
  export const buildPayload = (
    passwordSettings: PasswordSettings,
    policies: Policies,
    customPassword: string | null = null
  ) => ({
    ...passwordSettings,
    policies,
    password: customPassword,
  });
  
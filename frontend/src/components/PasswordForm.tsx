import React, { ChangeEvent } from 'react';
import { FaChevronDown, FaChevronUp } from 'react-icons/fa';
import { PolicyCheckbox } from './PolicyCheckbox';
import { InputField } from './InputField';

interface PasswordFormProps {
  policies: {
    uppercase: boolean;
    lowercase: boolean;
    numeric: boolean;
    special: boolean;
  };
  passwordSettings: {
    minLength: number;
    maxAttempts: number;
    availabilityTime: number;
  };
  onPolicyChange: (e: ChangeEvent<HTMLInputElement>) => void;
  onSettingChange: (e: ChangeEvent<HTMLInputElement>) => void;
  isPasswordVisible: boolean;
  onPasswordVisibilityToggle: () => void;
  password: string;
  onPasswordChange: (e: ChangeEvent<HTMLInputElement>) => void;
  onGeneratePassword: () => void;
  onSavePassword: () => void;
}

export const PasswordForm: React.FC<PasswordFormProps> = ({
  policies,
  passwordSettings,
  onPolicyChange,
  onSettingChange,
  isPasswordVisible,
  onPasswordVisibilityToggle,
  password,
  onPasswordChange,
  onGeneratePassword,
  onSavePassword,
}) => (
  <form className="bg-yellow-default p-6 rounded-lg w-full max-w-lg space-y-4">
    <div>
      <label className="text-black text-lg font-bold">Defina suas políticas de senha</label>
      <div className="mt-2 space-y-2">
        {Object.keys(policies).map((policy) => (
          <PolicyCheckbox
            key={policy}
            name={policy}
            label={`Min. 1 caractere ${policy === 'uppercase' ? 'maiúsculo' :
              policy === 'lowercase' ? 'minúsculo' :
              policy === 'numeric' ? 'numérico' : 'especial'}`}
            checked={policies[policy as keyof typeof policies]}
            onChange={onPolicyChange}
          />
        ))}
      </div>
    </div>

    {[
      { name: 'minLength', label: 'Número mínimo de caracteres' },
      { name: 'maxAttempts', label: 'Número máximo de consultas para a senha' },
      { name: 'availabilityTime', label: 'Tempo de disponibilidade da senha (em segundos)' },
    ].map((field) => (
      <InputField
        key={field.name}
        label={field.label}
        name={field.name}
        value={passwordSettings[field.name as keyof typeof passwordSettings]}
        onChange={onSettingChange}
      />
    ))}

    <div className="border-t border-black mt-4 pt-4">
      <button
        type="button"
        onClick={onPasswordVisibilityToggle}
        className="w-full text-black p-2 rounded-md text-left bg-transparent border border-black flex items-center justify-between"
      >
        <span>{isPasswordVisible ? 'Ocultar campo de senha' : 'Digite sua própria senha'}</span>
        {isPasswordVisible ? <FaChevronUp /> : <FaChevronDown />}
      </button>
      {isPasswordVisible && (
        <div className="mt-4">
          <label className="text-black text-lg font-bold">Senha</label>
          <input
            type="text"
            value={password}
            onChange={onPasswordChange}
            className="w-full p-2 mt-2 rounded-md"
          />
        </div>
      )}
    </div>

    <button
      type="button"
      onClick={isPasswordVisible ? onSavePassword : onGeneratePassword}
      className="w-full bg-black text-yellow-default p-2 rounded-md mt-4"
    >
      {isPasswordVisible ? 'Salvar Senha' : 'Gerar Senha'}
    </button>
  </form>
);

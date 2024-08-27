import React, { useState, ChangeEvent } from 'react';
import axios from 'axios';
import { PasswordForm } from '../components/PasswordForm';
import { validatePassword, buildPayload } from '../util/PasswordUtil';

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

export default function Home() {
  const [policies, setPolicies] = useState<Policies>({
    uppercase: true,
    lowercase: false,
    numeric: false,
    special: false,
  });

  const [passwordSettings, setPasswordSettings] = useState<PasswordSettings>({
    minLength: 6,
    maxAttempts: 2,
    availabilityTime: 180,
  });

  const [password, setPassword] = useState<string>('');
  const [isPasswordVisible, setIsPasswordVisible] = useState<boolean>(false);
  const [validationMessage, setValidationMessage] = useState<string>('Senha não atende as políticas escolhidas');
  const [isModalOpen, setIsModalOpen] = useState<boolean>(false);
  const [accessUrl, setAccessUrl] = useState<string>('');
  const [loading, setLoading] = useState<boolean>(false);

  const handleCheckboxChange = (e: ChangeEvent<HTMLInputElement>) => {
    setPolicies({ ...policies, [e.target.name]: e.target.checked });
  };

  const handleInputChange = (e: ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setPasswordSettings((prev) => ({
      ...prev,
      [name]: name === 'minLength' ? Math.max(6, parseInt(value)) : parseInt(value),
    }));
  };

  const handleGeneratePassword = () => {
    setLoading(true);
    axios.post('https://zgycemhwzl.execute-api.us-east-1.amazonaws.com/password', buildPayload(passwordSettings, policies))
      .then((response) => {
        console.log(JSON.stringify(response))
        if (response.status === 200) {
          setAccessUrl(`${window.location.origin}/view/${response.data.id}`);
          setIsModalOpen(true);
        } else {
          alert('Erro ao salvar a senha');
        }
      })
      .catch(() => alert('Erro ao salvar a senha'))
      .finally(() => setLoading(false));
  };

  const handleSavePassword = () => {
    if (validatePassword(password, policies, passwordSettings.minLength)) {
      setLoading(true);
      axios.post('https://zgycemhwzl.execute-api.us-east-1.amazonaws.com/password', buildPayload(passwordSettings, policies, password))
        .then((response) => {
          if (response.status === 200) {
            setAccessUrl(`${window.location.origin}/view/${response.data.id}`);
            setIsModalOpen(true);
          } else {
            alert('Erro ao salvar a senha');
          }
        })
        .catch(() => alert('Erro ao salvar a senha'))
        .finally(() => setLoading(false));
    } else {
      alert(validationMessage);
    }
  };

  if (loading) {
    return (
      <div className="bg-black min-h-screen flex items-center justify-center p-6">
        <div className="w-16 h-16 border-t-4 border-yellow-default border-solid rounded-full animate-spin"></div>
      </div>
    );
  }

  return (
    <div className="bg-black min-h-screen flex flex-col items-center justify-center space-y-6 p-6">
      <p className="text-yellow-default">Desafio Técnico TOTVS - Matheus Lima</p>
      <PasswordForm
        policies={policies}
        passwordSettings={passwordSettings}
        onPolicyChange={handleCheckboxChange}
        onSettingChange={handleInputChange}
        isPasswordVisible={isPasswordVisible}
        onPasswordVisibilityToggle={() => setIsPasswordVisible(!isPasswordVisible)}
        password={password}
        onPasswordChange={(e) => setPassword(e.target.value)}
        onGeneratePassword={handleGeneratePassword}
        onSavePassword={handleSavePassword}
      />

      {isModalOpen && (
        <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
          <div className="bg-white p-8 rounded-lg max-w-xl w-full">
            <h2 className="text-xl font-bold mb-4">URL de Acesso</h2>
            <p className="mb-4">
              <a href={accessUrl} target="_blank" rel="noopener noreferrer" className="bg-yellow-default text-white p-2 rounded-md block text-center">
                {accessUrl}
              </a>
            </p>
            <button
              onClick={() => setIsModalOpen(false)}
              className="w-full bg-black text-yellow-default p-2 rounded-md"
            >
              Fechar
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

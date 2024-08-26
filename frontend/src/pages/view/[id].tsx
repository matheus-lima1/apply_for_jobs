import { useEffect, useState } from 'react';
import { useRouter } from 'next/router';
import axios from 'axios';

const PasswordView = () => {
  const router = useRouter();
  const { id } = router.query;
  const [password, setPassword] = useState<string | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (id) {
      axios.get(`http://localhost:5000/password/${id}`)
        .then(response => {
          setPassword(response.data.password);
          setLoading(false);
        })
        .catch(error => {
          console.error('Erro na requisição:', error);
          setError(error.response.data.message);
          setLoading(false);
        });
    }
  }, [id]);

  if (loading) {
    return (
      <div className="bg-black min-h-screen flex items-center justify-center p-6">
        <div className="w-16 h-16 border-t-4 border-yellow-default border-solid rounded-full animate-spin"></div>
      </div>
    );
  }

  return (
    <div className="bg-black min-h-screen flex items-center justify-center p-6">
      <div className="bg-yellow-default p-8 rounded-lg w-full max-w-md">
        <div className="text-black text-center text-xl font-bold">
          {error ? error : password || 'Senha não encontrada'}
        </div>
      </div>
    </div>
  );
};

export default PasswordView;
